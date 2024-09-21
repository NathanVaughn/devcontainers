# syntax = edrevo/dockerfile-plus
ARG VERSION

FROM mcr.microsoft.com/devcontainers/python:${VERSION}
COPY --from=ghcr.io/astral-sh/uv:0.4.14 /uv /bin/uv

INCLUDE+ common/Dockerfile

USER vscode
ENV PATH="$PATH:/home/vscode/.local/bin"
COPY python/requirements.txt /tmp/
RUN --mount=type=cache,target=/home/vscode/.cache/,uid=1000 \
    xargs < /tmp/requirements.txt -n 1 uv tool install && sudo rm /tmp/requirements.txt \
 && poetry self add poetry-pre-commit-plugin
