from sokort.systems.grapes_gfs_gmf.graphics.an_aea import AnAeaPlotter


class Plotter(AnAeaPlotter):
    """
    850hPa 假相当位温

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=0313031802
    """
    plot_types = [
        "pte_p850_an_aea"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AnAeaPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_PTE_P850_AN_AEA.ncl"
