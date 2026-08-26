import os
from pathlib import Path
import sys
import re


class ProtoGenerationError(RuntimeError):
    """Raised when protobuf/gRPC code generation fails."""


def generate_protos():
    try:
        from grpc_tools import protoc
    except ImportError as e:
        raise ProtoGenerationError(
            "grpc_tools is required to generate protobuf/gRPC code but is not installed.\n"
            "Install it with `uv sync` (development) or `pip install grpcio-tools`."
        ) from e

    project_root = os.path.dirname(os.path.abspath(__file__))
    proto_dir = os.path.join(project_root, "proto")
    out_dir = os.path.join(project_root, "src/mcp_grpc_transport_proto")

    if not os.path.isdir(proto_dir):
        raise ProtoGenerationError(f"Proto source directory not found: {proto_dir}")

    os.makedirs(out_dir, exist_ok=True)

    proto_path = Path(proto_dir)
    proto_files = sorted(proto_path.glob("*.proto"))
    if not proto_files:
        raise ProtoGenerationError(f"No .proto files found in {proto_dir}; nothing to generate.")

    proto_names = [f.stem for f in proto_files]

    for file_path in proto_files:
        proto_file = os.path.join(proto_dir, file_path.name)

        print(f"Generating protos from {proto_file} into {out_dir}...")

        # Include the proto directory so imports work if there were any (mcp.proto imports google/protobuf/...)
        # We also include the project root just in case.

        # Including the grpc_tools _proto directory is required to find well-known types
        grpc_tools_include = os.path.join(os.path.dirname(protoc.__file__), "_proto")

        # protoc command arguments
        protoc_args = [
            "grpc_tools.protoc",
            f"-I{grpc_tools_include}",
            f"-I{proto_dir}",
            f"-I{project_root}",
            f"--python_out={out_dir}",
            f"--grpc_python_out={out_dir}",
            f"--pyi_out={out_dir}",
            proto_file,
        ]

        # Add well-known types include path if needed?
        # grpc_tools.protoc usually handles well-known types built-in or via site-packages.

        exit_code = protoc.main(protoc_args)

        if exit_code != 0:
            raise ProtoGenerationError(
                f"protoc failed with exit code {exit_code} while compiling {file_path.name}"
            )

        print("Success!\n")

    # Sanity check: protoc can report success (exit code 0) while still not
    # writing every expected output file, e.g. if out_dir isn't writable in
    # the way protoc expects. Fail loudly instead of shipping a partial package.
    expected_suffixes = ("_pb2.py", "_pb2_grpc.py", "_pb2.pyi")
    missing = [
        f"{name}{suffix}"
        for name in proto_names
        for suffix in expected_suffixes
        if not (Path(out_dir) / f"{name}{suffix}").exists()
    ]
    if missing:
        raise ProtoGenerationError(
            "protoc reported success but expected output files are missing: " + ", ".join(missing)
        )

    # Fix imports in generated files to be relative to the package root
    # to avoid import errors.
    print("Fixing imports in generated files...")
    patterns = ["*.py", "*.pyi"]
    for pattern in patterns:
        for py_file in Path(out_dir).glob(pattern):
            if not (py_file.name.endswith("_pb2.py") or py_file.name.endswith("_pb2_grpc.py") or py_file.name.endswith("_pb2.pyi")):
                continue

            content = py_file.read_text()
            original_content = content

            for name in proto_names:
                # Pattern to match 'import name_pb2' and 'import name_pb2_grpc'
                # We want to catch 'import name_pb2 as ...' or just 'import name_pb2'
                pattern = rf"^import ({name}_pb2(_grpc)?)\b"
                replacement = rf"from mcp_grpc_transport_proto import \1"
                content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

            if len(content) != len(original_content):
                print(f"  Fixed imports in {py_file.name}")
                py_file.write_text(content)

    print("All done!\n")


if __name__ == "__main__":
    try:
        generate_protos()
    except ProtoGenerationError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)
