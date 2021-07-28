FROM continuumio/miniconda

RUN groupadd -g 1004 jovyan \
    && useradd -u 1004 -g 1004 --create-home jovyan \
    && chown -R jovyan:jovyan /opt/conda \
    && chown -R jovyan:jovyan /srv

COPY sources.list /etc/apt/sources.list
RUN apt-get update -y && apt-get install -y gcc-6/stretch ksh fontconfig \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 6 \
    && apt-get install -y libgfortran3/stretch

COPY ncl_ncarg-6.4.0-Debian8.6_64bit_nodap_gnu492.tar.gz /srv/ncl/ncl.tar.gz
RUN cd /srv/ncl && tar zxf ncl.tar.gz && rm -rf ncl.tar.gz

USER jovyan

COPY .condarc ~/.condarc

RUN conda create -n py39 -c conda-forge -y \
    python=3.9 numpy scipy pandas xarray eccodes pyyaml jinja2 dask click tqdm imagemagick ipywidgets pillow \
    && conda clean --all -f -y

WORKDIR /home/jovyan

CMD ["conda", "run", "-n", "py39", "/bin/bash", "-c"]