# ensure git uses correct GPG application, and not imported git config
RUN git config --global gpg.program gpg2
# increase GPG timeout to 24 hours
# need to get default user, since Python and Node images use different user names
# Pythn = vscode
# Node = node
RUN user="$(ls -1 /home/ | head -n1)" \
  && mkdir -p /home/$user/.gnupg/ \
  && echo "default-cache-ttl 86400\nmax-cache-ttl 86400" > /home/$user/.gnupg/gpg-agent.conf \
  && chown -R $user:$user /home/$user/.gnupg/

LABEL org.opencontainers.image.source="https://github.com/NathanVaughn/devcontainers"
LABEL org.opencontainers.image.description="Pre-built devcontainer for Node with tools I like preinstalled."