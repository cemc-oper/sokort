# coding: utf-8
"""
850hPa 水汽通量散度
"""

from sokort.systems.grapes_gfs_gmf.graphics.an_aea import AnAeaPlotter


class Plotter(AnAeaPlotter):
    plot_types = [
        "qflx_p850_an_aea"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AnAeaPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_QFLX_P850_AN_AEA.ncl"
