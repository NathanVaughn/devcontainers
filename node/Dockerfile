# syntax = edrevo/dockerfile-plus

INCLUDE+ common/Dockerfile

# install fnm
RUN curl -fsSL https://fnm.vercel.app/install | bash -s -- --install-dir "/opt/fnm"
# update PATH
ENV PATH="$PATH:/opt/fnm"