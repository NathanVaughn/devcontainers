# Devcontainers

Pre-built devcontainers for Python and Node with tools I like preinstalled.

## Usage

In `.devcontainer/devcontainer.json`:

```json
{
    "image": "ghcr.io/nathanvaughn/devcontainers/python:latest",
}
```

or

```json
{
    "image": "ghcr.io/nathanvaughn/devcontainers/node:latest",
}
```

and

```json
{
    "mounts": [
        "source=devcontainer-profile-${containerWorkspaceFolderBasename},target=/home/dev/,type=volume"
    ]
}
```

## Installing Runtime

### Python

```bash
uv python install
```

### Node

```bash
n install auto
```
