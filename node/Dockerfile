ARG VERSION

FROM mcr.microsoft.com/devcontainers/javascript-node:${VERSION}

RUN git config --global user.email gpg.program gpg2

RUN npm install -g npm@latest
RUN npm install -g npm-check-updates
