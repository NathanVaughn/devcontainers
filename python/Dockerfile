# syntax = edrevo/dockerfile-plus

INCLUDE+ common/Dockerfile

COPY --from=ghcr.io/astral-sh/uv:0.5.13 /uv /uvx /opt/uv/bin/

# put saved tools outside user home
# so we can safely cache the user's home directory
ENV UV_TOOL_DIR=/opt/uv/tools
ENV UV_TOOL_BIN_DIR=/opt/uv/tools/bin
# update PATH
# include local bin for user insalled tools
ENV PATH="$PATH:/home/$USERNAME/.local/bin:/opt/uv/bin:/opt/uv/tools/bin"

# install tools
# need to chown directory afterwards as --mount causes it to be owned by root
RUN sudo mkdir -p $UV_TOOL_BIN_DIR \
 && sudo chmod -R 777 $UV_TOOL_DIR
RUN --mount=type=cache,target=/home/$USERNAME/.cache/uv,uid=1001,gid=1001 \
    --mount=type=bind,src=python/requirements.txt,dst=/tmp/requirements.txt \
    xargs < /tmp/requirements.txt -n 1 uv tool install \
 && sudo chown -R $USERNAME:$USERNAME /home/$USERNAME/.cache/

# reset env values
# seems that uv is not treating blank values as unset
# https://docs.astral.sh/uv/reference/cli/#uv-tool-dir
# https://github.com/astral-sh/uv/issues/8608
ENV UV_TOOL_DIR=/home/$USERNAME/.local/share/uv/tools
ENV UV_TOOL_BIN_DIR=/home/$USERNAME/.local/bin

# for some reason hardlinking fails
ENV UV_LINK_MODE=symlink

# force usage of uv managed python installs
ENV UV_PYTHON_PREFERENCE=only-managed
