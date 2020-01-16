# nwpc-graphics

封装中国气象局数值预报中心数值预报业务系统使用的图片制作脚本。

## 安装

从Github项目主页下载最新的代码，并使用pip安装。

本项目不包含业务系统使用的任何图片制作脚本，如果需要使用，请联系数值预报中心。

本项目针对气象局的内网环境开发，需要部署在挂载二级存储的服务器上。

## 使用

在安装好的Anaconda环境中启动 Jupyter Notebook。
执行下面的代码绘制并显示 GRAPES GFS 全球预报系统 2020 年 1 月 13 日 00 时次 24 小时的整层可降水量。

```python
from nwpc_graphics.systems.grapes_gfs_gmf import show_plot

show_plot("pwat_sfc_an_aea", "20200113", "00", "24h")
```

## LICENSE

Copyright 2020, perillaroc, 数值预报中心系统业务室系统运行科。

`nwpc-graphics` 以 [GPL-3.0](./LICENSE.md) 协议授权。

本项目涉及的数值预报业务系统及图片制作脚本版权均属于中国气象局数值预报中心。