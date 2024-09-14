from sokort.systems.cma_gfs.graphics.aea_an import AeaAnPlotter


class Plotter(AeaAnPlotter):
    """
    850hPa 水汽通量

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=0313032002
    """
    plot_types = [
        "cn.qflx_850"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AeaAnPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_QFLX_P850_AN_AEA.ncl"