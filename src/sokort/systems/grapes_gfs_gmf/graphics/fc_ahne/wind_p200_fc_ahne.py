from sokort.systems.grapes_gfs_gmf.graphics.fc_ahne import FcAhnePlotter


class Plotter(FcAhnePlotter):
    """
    200hPa 风场

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=03130104
    """
    plot_types = [
        "wind_p200_fc_ahne"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        FcAhnePlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_QV_P200+WIND_P200_FC_AHNE.ncl"
