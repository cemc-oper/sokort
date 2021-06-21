# coding: utf-8
"""
850hPa 比湿 + 850hPa 风场

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=03130205
"""
from sokort.systems.grapes_gfs_gmf.graphics.fc_aeua import FcAeuaPlotter


class Plotter(FcAeuaPlotter):
    plot_types = [
        "qv_p850_wind_p850_fc_aeua"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        FcAeuaPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_QV_P850+WIND_P850_FC_AEUA.ncl"
