# nwpc-oper/sokort-graphics

绘图脚本工具 sokort 镜像

## 编排

下载 nwpc-data 库和 sokort 库

```shell
mkdir -p lib
cd lib
git clone https://github.com/nwpc-oper/nwpc-data
git clone https://github.com/nwpc-oper/sokort
```

编排

```shell
docker build --rm -t nwpc-oper/sokort-base \
    --build-arg HTTP_PROXY=http://user:passwd@host:port \
    --build-arg HTTPS_PROXY=http://user:passwd@host:port \
    .
```

## 运行

挂载业务系统绘图脚本目录和二级存储目录，绘制 GRAPES GFS 系统整层可降水量图片

```shell
docker run --rm \
  -v /home/wangdp/project/graphics/operation/system:/srv/system \
  -v /sstorage1:/sstorage1 nwpc-oper/sokort-graphics \
  draw \
  --system=grapes_gfs_gmf \
  --plot-type=pwat_sfc_an_aea \
  --start-time=2021071100 \
  --forecast-time=24h
```