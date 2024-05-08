# ensure git uses correct GPG application, and not imported git config
RUN git config --global gpg.program gpg2
# increase GPG timeout to 24 hours
RUN mkdir -p /home/vscode/.gnupg/ \
  && echo "default-cache-ttl 86400\nmax-cache-ttl 86400" > /home/vscode/.gnupg/gpg-agent.conf \
  && chown -R vscode:vscode /home/vscode/.gnupg/

LABEL org.opencontainers.image.source="https://github.com/NathanVaughn/devcontainers"
LABEL org.opencontainers.image.description="Pre-built devcontainer for Node with tools I like preinstalled."