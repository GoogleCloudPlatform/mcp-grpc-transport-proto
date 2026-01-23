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

4. Build artifacts:
   The build artifacts (wheel and source distribution) will be located in the `dist/` directory.

### Publishing to PyPI

To upload the package to PyPI, you can use `uv publish`.

1. **Update Version**:
   Before publishing a new release, make sure to update the `version` field in `pyproject.toml`:
   ```toml
   [project]
   version = "0.1.1"  # Update to your desired version
   ```

2. **TestPyPI** (Recommended for testing):
   ```bash
   uv publish --publish-url https://test.pypi.org/legacy/
   ```

3. **PyPI** (Production):
   ```bash
   uv publish
   ```

   Note: You will need to configure your PyPI credentials (e.g., using a `.pypirc` file or environment variables like `UV_PUBLISH_TOKEN`).
