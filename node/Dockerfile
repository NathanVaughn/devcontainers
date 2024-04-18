ARG VERSION

FROM mcr.microsoft.com/devcontainers/javascript-node:${VERSION}

RUN git config --global gpg.program gpg2

RUN npm install -g npm@latest
RUN npm install -g npm-check-updates

LABEL org.opencontainers.image.source="https://github.com/NathanVaughn/devcontainers"
LABEL org.opencontainers.image.description="Pre-built devcontainer for Node with tools I like preinstalled."
