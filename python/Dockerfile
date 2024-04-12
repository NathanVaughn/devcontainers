ARG VERSION

FROM mcr.microsoft.com/devcontainers/python:${VERSION}

RUN git config --global user.email gpg.program gpg2

COPY requirements.txt /tmp/
RUN xargs < /tmp/requirements.txt -n 1 pipx install
RUN rm /tmp/requirements.txt

RUN poetry self add poetry-pre-commit-plugin