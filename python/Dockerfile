# syntax = edrevo/dockerfile-plus
ARG VERSION

FROM mcr.microsoft.com/devcontainers/python:${VERSION}
COPY --from=ghcr.io/astral-sh/uv:0.4.10 /uv /bin/uv

INCLUDE+ common/Dockerfile

ENV PATH="$PATH:/root/.local/bin"
COPY python/requirements.txt /tmp/
RUN --mount=type=cache,target=/root/.cache/ \
    xargs < /tmp/requirements.txt -n 1 uv tool install && sudo rm /tmp/requirements.txt \
 && poetry self add poetry-pre-commit-plugin
