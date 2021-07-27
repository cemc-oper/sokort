# nwpc-oper/graphics-hub

用于 sokort 的 JupyterHub 镜像

## 编排

编排镜像，如果在 CMA 集约化平台中，需要设置用于代理的环境变量。

```shell
docker build --rm -t nwpc-oper/graphics-hub \
    --build-arg HTTP_PROXY=http://user:passwd@host:port \
    --build-arg HTTPS_PROXY=http://user:passwd@host:port \
    .
```

## 运行

创建 jupyterhub 网络

```shell
docker network create jupyterhub
```

以交互方式运行镜像

```shell
docker run \
  --rm -it \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --net jupyterhub \
  --name graphics-hub-server \
  -p 9500:8000 \
  nwpc-oper/graphics-hub
```