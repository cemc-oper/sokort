from sokort.systems.cma_gfs.graphics.ahne_fc import AhneFcPlotter


class Plotter(AhneFcPlotter):
    """
    海平面气压

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=03130105
    """
    plot_types = [
        "north_polar.mslp"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AhneFcPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_MSLP_SFC_FC_AHNE.ncl"
