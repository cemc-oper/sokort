from sokort.systems.cma_gfs.graphics.aea_an import AeaAnPlotter


class Plotter(AeaAnPlotter):
    """
    850hPa 温度平流

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=03130313
    """
    plot_types = [
        "cn.tadv_850"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AeaAnPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_TADV_P850_AN_AEA.ncl"
