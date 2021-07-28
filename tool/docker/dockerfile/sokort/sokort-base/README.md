# nwpc-oper/sokort-base

绘图脚本工具 sokort 基础镜像

## 编排

下载 NCL 库，保存到当前目录

```shell
wget 
```

拉取镜像

```shell
docker pull continuumio/miniconda
```

编排

```shell
docker build --rm -t nwpc-oper/sokort-base \
    --build-arg HTTP_PROXY=http://user:passwd@host:port \
    --build-arg HTTPS_PROXY=http://user:passwd@host:port \
    .
```