from sokort.systems.cma_gfs.graphics.aeua_fc import AeuaFcPlotter


class Plotter(AeuaFcPlotter):
    """
    700hPa 比湿 + 700hPa 风场

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=03130204
    """
    plot_types = [
        "europe_asia.qv_700_wind_700"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AeuaFcPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_QV_P700+WIND_P700_FC_AEUA.ncl"
