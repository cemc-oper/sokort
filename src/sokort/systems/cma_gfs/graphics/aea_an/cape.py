from sokort.systems.cma_gfs.graphics.aea_an import AeaAnPlotter


class Plotter(AeaAnPlotter):
    """
    CAPE

    图片样例请访问NMC官网：
        http://www.nmc.cn/publish/nwpc/grapes_gfs/ea/cape.htm
    """
    plot_types = [
        "cn.cape"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AeaAnPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_CAPE_SFC_AN_AEA.ncl"
