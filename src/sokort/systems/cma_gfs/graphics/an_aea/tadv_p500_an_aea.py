from sokort.systems.cma_gfs.graphics.an_aea import AnAeaPlotter


class Plotter(AnAeaPlotter):
    """
    500hPa 温度平流

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=0313031302
    """
    plot_types = [
        "tadv_p500_an_aea"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AnAeaPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_TADV_P500_AN_AEA.ncl"
