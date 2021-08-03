.. sokort documentation master file, created by
   sphinx-quickstart on Mon Jul 12 03:26:12 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

欢迎来到 sokort 文档
==================================

NWPC Graphics Script Tool

封装中国气象局数值预报中心数值预报业务系统使用的图片制作脚本。

仅支持使用 NCL 绘图脚本，目前已支持的数值预报业务系统如下：

* GRAPES 全球预报系统 (`grapes_gfs`)
* GRAPES 区域预报系统 (`grapes_meso_3km`)
* GRAPES 区域台风预报系统 (`grapes_tym`)

用户指南
---------

.. toctree::
   :maxdepth: 2

   usage/installation
   usage/quickstart
   usage/cli
   usage/notebook
   usage/config

API 参考
---------

.. toctree::
   :maxdepth: 2

   api

索引和表格
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
