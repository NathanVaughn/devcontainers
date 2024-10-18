# syntax = edrevo/dockerfile-plus

INCLUDE+ common/Dockerfile

# move npm versions outside /usr/local
# controls install location
ENV N_PREFIX /home/code/.n
# controls where n installs node versions and tools
ENV PREFIX /opt/n
ENV PATH="$PATH:/home/code/.n/bin:/opt/n/bin"

# install https://github.com/tj/n
RUN cd /tmp/ \
 && git clone https://github.com/tj/n \
 && cd n \
 && git checkout v10.0.0 \
 && make install \
 && cd .. \
 && rm -rf n \
 && n lts

# install a few tools
RUN --mount=type=cache,target=/home/code/.npm/,uid=1001,gid=1001 \
    --mount=type=bind,src=node/.tool-versions,dst=/tmp/.tool-versions \
   xargs < /tmp/.tool-versions -n 1 npm install -g

# unset env values
ENV PREFIX ""