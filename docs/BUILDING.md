## Python Package

The Python package is located in `src/mcp_transport_proto`.

### Prerequisites

- Python 3.9+
- `uv` for dependency management

### Development

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Generate protobuf files:
   ```bash
   uv run python generate.py
   ```

3. Build the package:
   ```bash
   uv build
   ```
