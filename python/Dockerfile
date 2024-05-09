# syntax = edrevo/dockerfile-plus
ARG VERSION

FROM mcr.microsoft.com/devcontainers/python:${VERSION}

INCLUDE+ common/Dockerfile

COPY python/requirements.txt /tmp/
RUN --mount=type=cache,target=/root/.cache/ \
    xargs < /tmp/requirements.txt -n 1 pipx install && rm /tmp/requirements.txt \
 && poetry self add poetry-pre-commit-plugin
