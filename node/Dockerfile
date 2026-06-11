# syntax = edrevo/dockerfile-plus

INCLUDE+ common/Dockerfile

# install fnm
RUN mkdir -p /opt/nvm && \
    curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | NVM_DIR="/opt/nvm" bash
# update PATH
ENV PATH="$PATH:/opt/nvm"