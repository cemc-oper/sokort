from sokort.systems.cma_gfs.graphics.aeua_fc import AeuaFcPlotter


class Plotter(AeuaFcPlotter):
    """
    500hPa 高度场＋500hPa 温度场

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=03130202
    """
    plot_types = [
        "europe_asia.height_500_t_500"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AeuaFcPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_HGT_P500+TEMP_P500_FC_AEUA.ncl"
