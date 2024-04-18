ARG VERSION

FROM mcr.microsoft.com/devcontainers/python:${VERSION}

RUN git config --global gpg.program gpg2

COPY requirements.txt /tmp/
RUN xargs < /tmp/requirements.txt -n 1 pipx install
RUN rm /tmp/requirements.txt

RUN poetry self add poetry-pre-commit-plugin

LABEL org.opencontainers.image.source="https://github.com/NathanVaughn/devcontainers"
LABEL org.opencontainers.image.description="Pre-built devcontainer for Python with tools I like preinstalled."
