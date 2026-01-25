# MCP gRPC Streaming Extensions Proposal

## Overview

This proposal extends the base MCP gRPC protocol with true streaming capabilities. While the base `mcp.proto` provides gRPC transport for MCP operations, it uses mostly unary RPCs with a `dependent_requests`/`dependent_responses` pattern for server-to-client communication. This requires polling and doesn't leverage gRPC's native streaming capabilities.

The streaming extensions in `mcp_streaming.proto` address these limitations.

## Why Streaming Matters

### Current Limitations

1. **Polling for Server-Initiated Requests**: The base proto uses `dependent_requests` in responses, requiring clients to retry requests to receive server-initiated data.

2. **No Resource Change Notifications**: Clients must poll `ListResources` to detect changes.

3. **No Parallel Tool Execution**: Tools execute one at a time; no way to batch multiple tool calls and receive results as they complete.

4. **Large Resource Handling**: Resources must be buffered entirely; no chunking support.

5. **No Connection Multiplexing**: Each RPC is independent; no way to multiplex multiple operations over a shared connection.

### What Streaming Enables

| Use Case | Base Proto | With Streaming |
|----------|------------|----------------|
| Resource changes | Poll ListResources | WatchResources pushes notifications |
| Tool progress | Embedded in CallTool response | CallToolWithProgress streams updates |
| Multiple tools | Sequential calls | StreamToolCalls parallel execution |
| Large resources | Buffer entire response | ReadResourceChunked streams chunks |
| Connection reuse | New RPC per operation | Session multiplexes all operations |

## Extended Service Definition

```protobuf
service McpStreaming {
  // Connection lifecycle
  rpc Initialize(InitializeRequest) returns (InitializeResponse);
  rpc Ping(PingRequest) returns (PingResponse);

  // Bidirectional session - multiplex all operations
  rpc Session(stream SessionRequest) returns (stream SessionResponse);

  // Resource streaming
  rpc WatchResources(WatchResourcesRequest) returns (stream WatchResourcesResponse);
  rpc ReadResourceChunked(ReadResourceChunkedRequest) returns (stream ResourceChunk);

  // Tool streaming
  rpc StreamToolCalls(stream StreamToolCallsRequest) returns (stream StreamToolCallsResponse);
  rpc CallToolWithProgress(CallToolRequest) returns (stream CallToolProgressResponse);

  // Prompt streaming
  rpc StreamPromptCompletion(StreamPromptCompletionRequest) returns (stream StreamPromptCompletionResponse);
}
```

## Detailed Design

### Session RPC

The `Session` RPC provides bidirectional streaming for multiplexed operations:

```
Client                          Server
  |                               |
  |-- SessionRequest (init) ----->|
  |<-- SessionResponse (init) ----|
  |                               |
  |-- SessionRequest (list_tools) |
  |-- SessionRequest (call_tool)  |  (concurrent)
  |<-- SessionResponse (tool 1) --|
  |<-- SessionResponse (tool 2) --|
  |<-- SessionResponse (result) --|
  |                               |
  |-- SessionRequest (cancel) --->|
  |<-- SessionResponse (end) -----|
```

Key features:
- `message_id` / `in_reply_to` for request/response correlation
- Multiple concurrent requests over single stream
- Cancellation support via `CancelRequest`
- Explicit `StreamEnd` signals for multi-message responses

### WatchResources

Subscribe to resource changes:

```protobuf
rpc WatchResources(WatchResourcesRequest) returns (stream WatchResourcesResponse);
```

- URI glob patterns for filtering (e.g., `file:///data/*.json`)
- `include_initial` flag to receive current state first
- Change types: CREATED, UPDATED, DELETED
- Timestamp for ordering

### StreamToolCalls

Parallel tool execution:

```protobuf
rpc StreamToolCalls(stream StreamToolCallsRequest) returns (stream StreamToolCallsResponse);
```

- Client streams multiple tool call requests
- Server streams results as they complete
- Results may arrive in different order than requests
- Client-assigned `request_id` for correlation

### ReadResourceChunked

Stream large resources:

```protobuf
rpc ReadResourceChunked(ReadResourceChunkedRequest) returns (stream ResourceChunk);
```

- Configurable chunk size
- Chunk index for reassembly
- Total size hint when known
- Memory-efficient for large files

## Schema Manager Integration

### Motivation

MCP tools declare JSON schemas for their inputs. With gRPC, we have an opportunity to integrate with schema managers (similar to Confluent Schema Registry) for:

- **Dynamic schema discovery**: Fetch protobuf descriptors at runtime
- **Schema evolution**: Update tool schemas without redeploying clients
- **Gateway compatibility**: Proxies can validate/transform without compiled schemas
- **Multi-tenant systems**: Different tenants can have different tool schemas

### Proposed Extension Point

```protobuf
// Schema discovery service (optional companion to McpStreaming)
service McpSchemaRegistry {
  // Get the schema for a specific tool's input/output
  rpc GetToolSchema(GetToolSchemaRequest) returns (GetToolSchemaResponse);

  // Register a new tool schema version
  rpc RegisterToolSchema(RegisterToolSchemaRequest) returns (RegisterToolSchemaResponse);

  // List all registered schemas
  rpc ListSchemas(ListSchemasRequest) returns (ListSchemasResponse);

  // Check schema compatibility
  rpc CheckCompatibility(CheckCompatibilityRequest) returns (CheckCompatibilityResponse);
}

message GetToolSchemaRequest {
  string tool_name = 1;
  string version = 2;  // Optional, latest if not specified
}

message GetToolSchemaResponse {
  string tool_name = 1;
  string version = 2;
  google.protobuf.FileDescriptorProto descriptor = 3;
  string input_type_url = 4;
  string output_type_url = 5;
}
```

### Runtime Schema Resolution

```python
class SchemaProvider(Protocol):
    async def get_descriptor(self, type_url: str) -> FileDescriptorProto: ...
    async def register_schema(self, descriptor: FileDescriptorProto) -> str: ...

# Usage in transport
transport = GrpcClientTransport(
    target="localhost:50051",
    schema_provider=ConfluentSchemaProvider(registry_url="http://schema-registry:8081")
)
```

## Compatibility

The streaming extensions are **additive** - they don't modify the base `mcp.proto`:

1. Servers can implement both `Mcp` and `McpStreaming` services
2. Clients can detect streaming support via `Initialize` capabilities exchange
3. Fall back to base unary RPCs when streaming isn't available

## Implementation Status

A reference implementation exists in the [MCP Python SDK fork](https://github.com/ai-pipestream/python-sdk) with:

- Full server-side gRPC servicer with anyio streaming
- Client transport with session management
- All streaming RPCs implemented and tested
- 19 gRPC-specific tests passing

## Next Steps

1. **Feedback on proto design**: Are the message structures appropriate?
2. **Capability negotiation**: How should clients discover streaming support?
3. **Schema manager integration**: Should this be a separate service or extension?
4. **Tunneling support**: How should gateways handle these streaming RPCs?

## References

- [Google Cloud Blog: gRPC as Native Transport for MCP](https://cloud.google.com/blog/products/networking/grpc-as-a-native-transport-for-mcp)
- [MCP Specification](https://modelcontextprotocol.io/specification/2025-06-18/)
- [gRPC Streaming Patterns](https://grpc.io/docs/what-is-grpc/core-concepts/#server-streaming-rpc)
