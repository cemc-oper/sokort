from sokort.systems.cma_gfs.graphics.ahne_fc import AhneFcPlotter


class Plotter(AhneFcPlotter):
    """
    850hPa 温度

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=03130103
    """
    plot_types = [
        "north_polar.t_850"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AhneFcPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_TEMP_P850_FC_AHNE.ncl"
