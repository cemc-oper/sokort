from sokort.systems.cma_gfs.graphics.aea_fc import AeaFcPlotter


class Plotter(AeaFcPlotter):
    """
    700hPa 流场

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=03130309
    """
    plot_types = [
        "cn.wind_streamline_700"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AeaFcPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_STR_P700_FC_AEA.ncl"
