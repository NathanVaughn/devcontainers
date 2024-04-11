ARG VERSION

FROM mcr.microsoft.com/devcontainers/python:${VERSION}

COPY requirements.txt /tmp/
RUN xargs < /tmp/requirements.txt -n 1 pipx install
RUN rm /tmp/requirements.txt
