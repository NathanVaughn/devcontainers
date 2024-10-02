# syntax = edrevo/dockerfile-plus
ARG VERSION

FROM mcr.microsoft.com/devcontainers/python:${VERSION}
COPY --from=ghcr.io/astral-sh/uv:0.4.18 /uv /uvx /bin/

INCLUDE+ common/Dockerfile

# put saved tools outside user home
# so we can safely cache the user's home directory
ENV UV_TOOL_DIR /opt/uv/
ENV UV_TOOL_BIN_DIR /opt/uv/tools
# update PATH
ENV PATH="$PATH:/opt/uv/tools"

# install tools
COPY python/requirements.txt /tmp/
RUN --mount=type=cache,target=/root/.cache/ \
    xargs < /tmp/requirements.txt -n 1 uv tool install && rm /tmp/requirements.txt \
 && poetry self add poetry-pre-commit-plugin \
 && chmod -R a+rx /opt/uv/
# unset env values
ENV UV_TOOL_DIR ""
ENV UV_TOOL_BIN_DIR ""
# update PATH
ENV PATH="$PATH:/home/vscode/.local/bin"

# for some reason hardlinking fails
ENV UV_LINK_MODE=symlink