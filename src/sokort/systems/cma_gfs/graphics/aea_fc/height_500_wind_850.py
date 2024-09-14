from sokort.systems.cma_gfs.graphics.aea_fc import AeaFcPlotter


class Plotter(AeaFcPlotter):
    """
    500hPa 高度场 + 850hPa 风场

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=03130306
    """
    plot_types = [
        "cn.height_500_wind_850"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AeaFcPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_HGT_P500+WIND_P850_FC_AEA.ncl"
