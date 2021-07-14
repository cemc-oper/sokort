***********
命令行工具
***********

sokort 提供命令行工具，用于绘制或显示图片。

使用
=========

使用 ``python -m sokort`` 运行命令行工具，如下所示：

.. code-block:: bash

    python -m sokort show \
        --system=grapes_gfs_gmf \
        --plot-type=pwat_sfc_an_aea \
        --start-time=2021071100 \
        --forecast-time=24h

命令
=========

包含三个子命令：

- ``draw``：绘图图片
- ``show``：绘制并显示图片
- ``list``：列出支持的绘图类型

参数说明
---------

``draw`` 与 ``show`` 命令共享通用参数

- `--config`：配置文件路径
- `--system`：业务系统名称，例如
    - `grapes_gfs`
    - `grapes_meso_3km`
    - `grapes_tym`
- `--plot-type`：绘图类型，例如 `pwat_sfc_an_aea` 表示整层可降水量
- `--start-time`：起报时刻，`YYYYMMDDHH` 或 `pd.to_timestamp` 支持的时间字符串
- `--forecast-time`：预报时效，`HHh` 或 `pd.to_timedelta` 支持的时间段字符串
- `--data-dir`：预报数据保存位置，默认由系统自动查找 (使用 nwpc-data 库)
- `--work-dir`：绘图运行目录，默认由系统根据配置文件中的设置自动创建

list
---------

列出支持的绘图类型

.. code-block:: bash

    python -m sokort list --system grapes_gfs_gmf

.. code-block::

    hgt_p500_fc_ahne
    wind_p200_fc_ahne
    temp_p850_fc_ahne
    mslp_sfc_fc_ahne
    hgt_p200_fc_ahne
    t2m_extrems.max_sfc_an_aea
    t2m_extrems.min_sfc_an_aea
    hgt_p500_wind_p850_fc_aeua
    ...
