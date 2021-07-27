FROM nwpc-oper/base-notebook:latest

USER root
RUN apt-get update -y && apt-get install -y g++-6 ksh && \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 6 && \
    apt-get install libgfortran3

COPY lib /srv/lib
COPY ncl_ncarg-6.4.0-Debian8.6_64bit_nodap_gnu492.tar.gz /srv/ncl/ncl.tar.gz
RUN cd /srv/ncl && tar zxf ncl.tar.gz && rm -rf ncl.tar.gz

USER jovyan

RUN conda install -c conda-forge -y imagemagick && \
    conda clean --all -f -y

RUN mkdir -p ~/.config/nwpc-oper && \
    cp -r /srv/lib/sokort/tool/docker/config/sokort ~/.config/nwpc-oper/sokort && \
    cd /srv/lib/sokort && \
    python3 -m pip install .

ENV NCARG_ROOT="/srv/ncl"
ENV PATH="/srv/ncl/bin:${PATH}"

WORKDIR /srv