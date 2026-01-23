import os
import sys
import shutil
from grpc_tools import protoc

def generate_protos():
    project_root = os.path.dirname(os.path.abspath(__file__))
    proto_dir = os.path.join(project_root, "proto")
    out_dir = os.path.join(project_root, "src/mcp_transport_proto")

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    proto_file = os.path.join(proto_dir, "mcp.proto")
    
    # Check if proto file exists
    if not os.path.exists(proto_file):
        print(f"Error: {proto_file} not found.")
        sys.exit(1)

    print(f"Generating protos from {proto_file} into {out_dir}...")
    
    # Include the proto directory so imports work if there were any (mcp.proto imports google/protobuf/...)
    # We also include the project root just in case.
    
    # Including the grpc_tools _proto directory is required to find well-known types
    # like google/protobuf/struct.proto, timestamp.proto, etc.
    # See: https://github.com/grpc/grpc/issues/15918
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
        
    print("Success!")
    
    # Fix imports in generated files to be relative or absolute to the package?
    # Protobuf 3 python generation usually generates imports like `import mcp_pb2 as ...`
    # If mcp_pb2 is in the same directory, it works if the directory is in path, or via relative import fix.
    # However, since we are generating into the package, `import mcp_pb2` might fail if we import from outside.
    # But here we only have one proto file, so it shouldn't import other local protos.
    # It imports `google.protobuf...` which is fine.

if __name__ == "__main__":
    generate_protos()
