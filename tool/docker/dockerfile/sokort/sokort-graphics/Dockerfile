FROM nwpc-oper/sokort-base:latest

USER jovyan
COPY lib /srv/lib

SHELL ["conda", "run", "-n", "py39", "/bin/bash", "-c"]

RUN mkdir -p ~/.config/nwpc-oper \
    && cp -r /srv/lib/sokort/tool/docker/config/sokort ~/.config/nwpc-oper/sokort \
    && cd /srv/lib/nwpc-data \
    && python3 -m pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && python3 -m pip install . \
    && cd /srv/lib/sokort \
    && python -m pip install .

ENV NCARG_ROOT="/srv/ncl"
ENV PATH="/srv/ncl/bin:${PATH}"

WORKDIR /home/jovyan

ENTRYPOINT ["conda", "run", "-n", "py39", "python", "-m", "sokort"]