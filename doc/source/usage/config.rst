***********
配置
***********

配置文件用于设置业务系统绘图脚本库目录和绘图环境加载脚本，参看项目源码的 `config` 文件夹。

配置文件默认放在 `$HOME/.config/nwpc-oper/sokort` 目录中。

配置目录结构
============

..

    config.yaml
    load_env.sh
    systems/
        grapes_gfs_gmf.yaml
        grapes_meso_3km.yaml
        grapes_tym.yaml
        ...


配置选项
===========

config.yaml
------------

主配置文件

.. code-block:: yaml

    ncl:
      ncl_lib: "/some/path/ncllib/"
      geodiag_root: "/some/path/GEODIAG/"
      load_env_script: "./load_env.sh"

    general:
      run_base_dir: "/tmp"

    config:
      systems_dir: "./systems"

选项说明：

* ``ncl.ncl_lib``：ncllib 库目录，通常包含在业务系统绘图系统中
* ``ncl.geodiag_root``：GEODIAG 库目录，单独设置
* ``ncl.load_env_script``：加载绘图环境的 Shell 脚本，一般为加载 NCL 环境，默认不用修改
* ``general.run_base_dir``：自动生成运行目录的默认根目录
* ``config.systems_dir``：各系统配置文件保存目录，无需修改


load_env.sh
-------------

绘图环境加载脚本。例如在 CMA-PI 上需要加载 NCL 环境

.. code-block:: bash

    #!/bin/bash
    module load mathlib/ncl_ncarg/6.4.0/gnu


grapes_gfs_gmf.yaml
---------------------

GRAPES GFS 全球预报系统配置文件

.. code-block:: yaml

    system:
      ncl_dir: "${GRAPHIC_BASE}/program/gmf-grapes-gfs-post-program/tograph/script/"
      script_dir: "${GRAPHIC_BASE}/program/gmf-grapes-gfs-post-program/tograph/script/"

    components:
      gams:
        ncl_dir: "${GRAPHIC_BASE}/program/gmf-grapes-gfs-post-program/tograph/script/GAMS-A/"
      typhoon:
        ncl_dir: "${GRAPHIC_BASE}/program/gmf-grapes-gfs-post-program/tograph/script/typhoon/"


* ``system.ncl_dir``：NCL 脚本目录
* ``system.script_dir``：NCL 脚本目录
* ``components``：为绘图组件配置参数
* ``components.gams.ncl_dir``：GAMS 类型绘图的 NCL 脚本目录