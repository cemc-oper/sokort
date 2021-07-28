# nwpc-oper/base-notebook

基础镜像

## 编排

下载 nwpc-data 库

```shell
mkdir -p lib
cd lib
git clone https://github.com/nwpc-oper/nwpc-data
cd ..
```

拉取基础镜像

```shell
docker pull jupyter/scipy-notebook
```

编排镜像，如果在 CMA 集约化平台中，需要设置用于代理的环境变量。

```shell
docker build --rm -t nwpc-oper/base-notebook \
    --build-arg HTTP_PROXY=http://user:passwd@host:port \
    --build-arg HTTPS_PROXY=http://user:passwd@host:port \
    .
```