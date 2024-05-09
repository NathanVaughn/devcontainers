# syntax = edrevo/dockerfile-plus
ARG VERSION

FROM mcr.microsoft.com/devcontainers/javascript-node:${VERSION}

INCLUDE+ common/Dockerfile

RUN --mount=type=cache,target=/root/.npm/ \
    npm install -g npm@latest \
 && npm install -g npm-check-updates
