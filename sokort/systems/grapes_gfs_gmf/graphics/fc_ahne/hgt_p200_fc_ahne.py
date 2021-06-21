# coding: utf-8
"""
200hPa高度 + 200hPa风场

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=031301
"""
from sokort.systems.grapes_gfs_gmf.graphics.fc_ahne import FcAhnePlotter


class Plotter(FcAhnePlotter):
    plot_types = [
        "hgt_p200_fc_ahne"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        FcAhnePlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_HGT_P200_FC_AHNE.ncl"
