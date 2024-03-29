from sokort.systems.grapes_gfs_gmf.graphics.fc_aea import FcAeaPlotter


class Plotter(FcAeaPlotter):
    """
    500hPa 风场

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=0313030403
    """
    plot_types = [
        "wind_p500_fc_aea"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        FcAeaPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_WIND_P500_FC_AEA.ncl"
