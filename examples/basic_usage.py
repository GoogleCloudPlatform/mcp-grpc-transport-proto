from mcp_transport_proto import mcp_pb2, mcp_messages_pb2
from google.protobuf import struct_pb2

def main():
    print("=== MCP Proto Basic Usage Example ===\n")

    # 1. Create a ListResourcesRequest
    print("1. Creating a ListResourcesRequest")
    list_req = mcp_messages_pb2.ListResourcesRequest()
    # Populate common fields if needed, e.g., metadata
    list_req.common.metadata.update({"user_id": "12345"})
    print(f"ListResourcesRequest:\n{list_req}")

    # 2. Create a CallToolRequest
    print("\n2. Creating a CallToolRequest")
    call_req = mcp_messages_pb2.CallToolRequest()
    call_req.request.name = "calculator"

    # Arguments are a google.protobuf.Struct
    call_req.request.arguments.update({
        "operation": "add",
        "a": 10,
        "b": 20
    })

    print(f"CallToolRequest:\n{call_req}")

    # 3. Create a CallToolResponse
    print("\n3. Creating a CallToolResponse")
    call_resp = mcp_messages_pb2.CallToolResponse()

    # Add text content
    text_content = call_resp.content.add()
    text_content.text.text = "The result is 30"

    print(f"CallToolResponse:\n{call_resp}")

    print("\n=== Done ===")

if __name__ == "__main__":
    main()
