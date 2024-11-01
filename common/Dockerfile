FROM docker.io/library/ubuntu:24.04

# needed for oh-my-posh https://github.com/JanDeDobbeleer/oh-my-posh/discussions/3691#discussioncomment-5555932
ENV USERNAME=dev
# ubuntu image comes with ubuntu user at uid 1000
ENV USER_UID=1001
ENV USER_GID=1001

# install common tools
ENV DEBIAN_FRONTEND=noninteractive
RUN --mount=target=/var/lib/apt,type=cache,sharing=locked \
    --mount=target=/var/cache/apt,type=cache,sharing=locked \
    rm -f /etc/apt/apt.conf.d/docker-clean \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    apt-utils \
    bash-completion \
    bat \
    build-essential \
    ca-certificates\
    coreutils \
    curl \
    gnupg2 \
    grep \
    htop \
    iproute2 \
    iputils-ping \
    jq \
    less \
    locales \
    lsb-release \
    nano\
    net-tools\
    python-is-python3 \
    rsync\
    sed \
    software-properties-common\
    sudo\
    unzip \
    wget \
    which \
 && apt-add-repository ppa:git-core/ppa \
 && apt-get install -y --no-install-recommends git

# create opt directory
RUN mkdir -p /opt/ \
 && chmod -R 777 /opt/
ENV PATH="$PATH:/opt"

# add a non-root user
# https://github.com/devcontainers/features/blob/125f6b0071597a59f3ccbefaf9145b5867528ae3/src/common-utils/main.sh#L422-L438
# https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user#_creating-a-nonroot-user
RUN groupadd --gid $USER_GID $USERNAME \
 && useradd --uid $USER_UID --gid $USERNAME -m $USERNAME \
 && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
 && chmod 0440 /etc/sudoers.d/$USERNAME

# set default user
USER $USERNAME

# ensure git uses correct GPG application, and not imported git config
RUN git config --global gpg.program gpg2

# increase GPG timeout to 24 hours
RUN mkdir -p /home/$USERNAME/.gnupg/ \
 && echo "default-cache-ttl 86400\nmax-cache-ttl 86400" > /home/$USERNAME/.gnupg/gpg-agent.conf \
 && chown -R $USERNAME:$USERNAME /home/$USERNAME/.gnupg/

# install oh-my-posh
# renovate: datasource=github-releases depName=oh-my-posh packageName=JanDeDobbeleer/oh-my-posh
ENV OMP_VERSION=v23.20.3
RUN curl -s https://ohmyposh.dev/install.sh | bash -s -- -d /opt/ -v $OMP_VERSION \
 && echo 'eval "$(/opt/oh-my-posh init bash)"' >> ~/.bashrc

# set default shell for vscode
ENV SHELL=/bin/bash

# add labels
LABEL org.opencontainers.image.source="https://github.com/NathanVaughn/devcontainers"
LABEL org.opencontainers.image.description="Pre-built devcontainer with tools I like preinstalled."
