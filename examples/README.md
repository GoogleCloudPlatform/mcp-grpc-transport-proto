# Examples

This directory contains examples of how to use the `mcp-grpc-transport-proto` package.

## Prerequisites

The examples assume that the `mcp-transport-proto` package is installed in your python environment.

### Using `uv` (Recommended)

Sync the project dependencies (this installs the package in editable mode):

```bash
uv sync
```

### Using `pip`

Install the package from the root of the repository:

```bash
pip install .
```

## Basic Usage

`basic_usage.py` demonstrates how to import the generated protobuf classes and create messages.

To run it using `uv`:

```bash
uv run python examples/basic_usage.py
```

To run it using standard `python` (after `pip install .`):

```bash
python examples/basic_usage.py
```
