# coding: utf-8
"""
500hPa 高度场＋500hPa 温度场

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=03130202
"""
from sokort.systems.grapes_gfs_gmf.graphics.fc_aeua import FcAeuaPlotter


class Plotter(FcAeuaPlotter):
    plot_types = [
        "hgt_p500_temp_p500_fc_aeua"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        FcAeuaPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_HGT_P500+TEMP_P500_FC_AEUA.ncl"
