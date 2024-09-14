from sokort.systems.cma_gfs.graphics.aeua_fc import AeuaFcPlotter


class Plotter(AeuaFcPlotter):
    """
    500hPa 高度场＋850hPa 风场

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=03130203
    """
    plot_types = [
        "europe_asia.height_500_wind_850"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AeuaFcPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_HGT_P500+WIND_P850_FC_AEUA.ncl"
