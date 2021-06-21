# coding: utf-8
"""
850hPa 温度

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=03130103
"""
from sokort.systems.grapes_gfs_gmf.graphics.fc_ahne import FcAhnePlotter


class Plotter(FcAhnePlotter):
    plot_types = [
        "temp_p850_fc_ahne"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        FcAhnePlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_TEMP_P850_FC_AHNE.ncl"
