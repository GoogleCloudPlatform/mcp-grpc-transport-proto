# Model Context Protocol (MCP) - gRPC Transport Protobuf Definitions

This repository contains the Protocol Buffer definitions (`.proto`) and generated Python bindings for implementing the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) over gRPC.

The definitions are currently in sync with the MCP schema version [2026-07-28](https://github.com/modelcontextprotocol/modelcontextprotocol/tree/main/schema/2026-07-28).

For additional context, see: [gRPC as a Native Transport for MCP](https://cloud.google.com/blog/products/networking/grpc-as-a-native-transport-for-mcp).

## Repository Structure

*   `proto/`: Contains the raw Protocol Buffer definitions.
    *   [mcp.proto](file:///usr/local/google/home/bpawan/workspace/mcp-grpc-transport-proto/proto/mcp.proto): Defines the `Mcp` gRPC service.
    *   [mcp_messages.proto](file:///usr/local/google/home/bpawan/workspace/mcp-grpc-transport-proto/proto/mcp_messages.proto): Defines the request/response payloads.
*   `src/mcp_grpc_transport_proto/`: The Python package. The compiled Protobuf and gRPC code is generated into this directory at build/install time and is not checked into git.
*   `generate.py`: A utility script to compile the `.proto` files into the Python package.
*   `examples/`: Contains example Python code demonstrating how to construct and use these messages.

## Getting Started (Python)

### Prerequisites
*   Python 3.9+
*   `uv` (recommended) or `pip`

### Installation
To install the package in editable mode:
```bash
uv sync
# or
pip install .
```

### Running Examples
See the [examples/README.md](file:///usr/local/google/home/bpawan/workspace/mcp-grpc-transport-proto/examples/README.md) for details on running the basic usage example:
```bash
uv run python examples/basic_usage.py
```

### Generating Protos
The compiled Python bindings are generated automatically whenever the package is built or installed (e.g. via `uv sync`, `pip install .`, or `uv build`) — they're not checked into git. If you modify the `.proto` files and want to regenerate them without a full install, run:
```bash
uv run python generate.py
```

## Usage in Other Languages

Because these are standard Protocol Buffers, you can generate client and server stubs for any gRPC-supported language (Go, Java, Rust, C++, Node.js, etc.) using `protoc` with the appropriate plugins.

## Evolution and Compatibility

This schema is designed to evolve alongside the official MCP specification.
*   Only non-breaking changes (such as adding optional fields) will be made.
*   The schema avoids protobuf `oneof` fields to ensure forward compatibility when new message types are added.
