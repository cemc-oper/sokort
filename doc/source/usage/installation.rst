*******
安装
*******

从 Github 项目主页下载最新的代码，并使用 pip 安装。

.. code-block:: bash

    git clone https://github.com/nwpc-oper/sokort
    cd sokort
    pip install .

本项目不包含业务系统使用的任何图片库及图形绘制脚本，如果需要使用，请联系数值预报中心。

本项目针对气象局的内网环境开发，需要部署在 CMA-PI 高性能计算机或挂载二级存储的服务器上。

额外 Python 包
===============

请安装下面未使用 pip 管理的 Python 包：

- `nwpc-data <https://github.com/nwpc-oper/nwpc-data>`_