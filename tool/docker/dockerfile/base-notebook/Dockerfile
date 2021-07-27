FROM jupyter/scipy-notebook:latest

COPY lib /srv/lib
COPY .condarc ~/.condarc

RUN conda install -c conda-forge -y eccodes cfgrib protobuf requests && \
    conda clean --all -f -y

RUN cd /srv/lib/nwpc-data && \
    python3 -m pip install .

USER root
COPY sources.list /etc/apt/sources.list

USER jovyan

WORKDIR /srv
