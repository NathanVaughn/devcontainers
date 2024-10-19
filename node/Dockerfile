# syntax = edrevo/dockerfile-plus

INCLUDE+ common/Dockerfile

# move npm versions outside /usr/local
# controls install location
ENV N_PREFIX /home/code/.n
# controls where n installs node versions and tools
ENV PREFIX /opt/n
# update PATH
ENV PATH="$PATH:/home/code/.n/bin:/opt/n/bin"

# install n
# renovate: datasource=github-releases depName=n packageName=tj/n
ENV N_VERSION=v10.0.0
RUN cd /tmp/ \
 && git clone https://github.com/tj/n \
 && cd n \
 && git checkout $N_VERSION \
 && make install \
 && cd .. \
 && rm -rf n \
 && n lts

# install a few tools
# need to chown directory afterwards as --mount causes it to be owned by root
RUN --mount=type=cache,target=/home/code/.npm/,uid=1001,gid=1001 \
    --mount=type=bind,src=node/.tool-versions,dst=/tmp/.tool-versions \
    xargs < /tmp/.tool-versions -n 1 npm install -g \
 && sudo chown -R code:code /home/code/.npm/

# unset env values
ENV PREFIX ""