# Devcontainers

Pre-built devcontainers for Python and Node with tools I like preinstalled.

## Usage

In `.devcontainer/devcontainer.json`:

```json
{
    "image": "ghcr.io/nathanvaughn/devcontainers/python:latest",
    "mounts": [
        "source=devcontainer-profile,target=/home/vscode/,type=volume"
    ]
}
```

or

```json
{
    "image": "ghcr.io/nathanvaughn/devcontainers/node:latest",
    "mounts": [
        "source=devcontainer-profile,target=/home/vscode/,type=volume"
    ]
}
```
