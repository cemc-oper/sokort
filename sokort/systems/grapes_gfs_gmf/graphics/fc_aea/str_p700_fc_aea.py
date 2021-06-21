# coding: utf-8
"""
700hPa 流场

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=03130309
"""
from sokort.systems.grapes_gfs_gmf.graphics.fc_aea import FcAeaPlotter


class Plotter(FcAeaPlotter):
    plot_types = [
        "str_p700_fc_aea"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        FcAeaPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_STR_P700_FC_AEA.ncl"
