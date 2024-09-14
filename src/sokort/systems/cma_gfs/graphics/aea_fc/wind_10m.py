from sokort.systems.cma_gfs.graphics.aea_fc import AeaFcPlotter
from sokort.util import get_forecast_hour


class Plotter(AeaFcPlotter):
    """
    10m 风场

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=0313030405
    """
    plot_types = [
        "cn.wind_10m"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AeaFcPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_WIND_10M_FC_AEA.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than 0h.")

    def _check_forecast_time(self) -> bool:
        forecast_hour = get_forecast_hour(self.forecast_timedelta)
        return not forecast_hour == 0
