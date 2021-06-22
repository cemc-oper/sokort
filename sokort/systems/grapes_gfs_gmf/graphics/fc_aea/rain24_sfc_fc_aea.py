# coding: utf-8
"""
24小时累计降水

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=03130302
"""
from sokort.systems.grapes_gfs_gmf.graphics.fc_aea import FcAeaPlotter
from sokort._util import get_forecast_hour


class Plotter(FcAeaPlotter):
    plot_types = [
        "rain24_sfc_fc_aea"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        FcAeaPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_RAIN24_SFC_FC_AEA.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than 24h.")

        forecast_hour = get_forecast_hour(self.forecast_timedelta)
        self.min_forecast_time = f"{forecast_hour - 24:03}"
        self.max_forecast_time = f"{forecast_hour:03}"

    def _check_forecast_time(self) -> bool:
        forecast_hour = get_forecast_hour(self.forecast_timedelta)
        return forecast_hour >= 24
