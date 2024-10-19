# syntax = edrevo/dockerfile-plus

INCLUDE+ common/Dockerfile

COPY --from=ghcr.io/astral-sh/uv:0.4.24 /uv /uvx /bin/

# put saved tools outside user home
# so we can safely cache the user's home directory
ENV UV_TOOL_DIR /opt/uv/
ENV UV_TOOL_BIN_DIR /opt/uv/tools
# update PATH
ENV PATH="$PATH:/home/code/.local/bin:/opt/uv/tools"

# install tools
# need to chown directory afterwards as --mount causes it to be owned by root
RUN --mount=type=cache,target=/home/code/.cache/uv,uid=1001,gid=1001 \
    --mount=type=bind,src=python/requirements.txt,dst=/tmp/requirements.txt \
    xargs < /tmp/requirements.txt -n 1 uv tool install \
 && sudo chown -R code:code /home/code/.cache/

# unset env values
ENV UV_TOOL_DIR ""
ENV UV_TOOL_BIN_DIR ""

# for some reason hardlinking fails
ENV UV_LINK_MODE=symlink

# force usage of uv managed python installs
ENV UV_PYTHON_PREFERENCE=only-managed