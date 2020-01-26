# coding: utf-8
"""
2m 温度

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=03130329
"""

from nwpc_graphics.systems.grapes_gfs_gmf.graphics.an_aea import AnAeaPlotter


class Plotter(AnAeaPlotter):
    plot_types = [
        "t2m_sfc_an_aea"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        AnAeaPlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "GFS_GRAPES_T2M_SFC_AN_AEA.ncl"
