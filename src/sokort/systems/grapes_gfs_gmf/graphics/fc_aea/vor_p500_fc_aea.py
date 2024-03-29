from sokort.systems.grapes_gfs_gmf.graphics.fc_aea import FcAeaPlotter


class Plotter(FcAeaPlotter):
    """
    500hPa 相对涡度

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=03130316
    """
    plot_types = [
        "vor_p500_fc_aea"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        FcAeaPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_VOR_P500_FC_AEA.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than 0h.")

    def _check_forecast_time(self) -> bool:
        return not int(self.forecast_hour) == 0
