import os
from pathlib import Path
import sys
import shutil
import re
from grpc_tools import protoc


def generate_protos():
    project_root = os.path.dirname(os.path.abspath(__file__))
    proto_dir = os.path.join(project_root, "proto")
    out_dir = os.path.join(project_root, "src/mcp_transport_proto")

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    proto_path = Path(proto_dir)
    suffix = ".proto"
    proto_files = list(proto_path.glob(f"*{suffix}"))
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
            print("Failed to generate protos.")
            sys.exit(exit_code)

        print("Success!\n")


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
                replacement = rf"from mcp_transport_proto import \1"
                content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

            if len(content) != len(original_content):
                print(f"  Fixed imports in {py_file.name}")
                py_file.write_text(content)

    print("All done!\n")


if __name__ == "__main__":
    generate_protos()
