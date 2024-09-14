from sokort.systems.cma_gfs.graphics.ahne_fc import AhneFcPlotter


class Plotter(AhneFcPlotter):
    """
    500hPa高度 + 500hPa风场

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=03130102
    """
    plot_types = [
        "north_polar.height_500"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AhneFcPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_HGT_P500_FC_AHNE.ncl"