# coding: utf-8
"""
CAPE

图片样例请访问NMC官网：
    http://www.nmc.cn/publish/nwpc/grapes_gfs/ea/cape.htm
"""

from sokort.systems.grapes_gfs_gmf.graphics.an_aea import AnAeaPlotter


class Plotter(AnAeaPlotter):
    plot_types = [
        "cape_sfc_an_aea"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AnAeaPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_CAPE_SFC_AN_AEA.ncl"
