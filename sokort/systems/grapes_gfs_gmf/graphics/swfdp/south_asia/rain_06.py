"""
South Asia, 6hr Accumulated Precipitation

图片样例请访问 WMC-BJ 官网：
    http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES-GFS-0521/ER6_ASA_L88_P9/index2.html
"""
from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class SouthAsiaRain06Plotter(SwfdpPlotter):
    plot_types = [
        "swfdp.south_asia.rain_06"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthAsiaRain06Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sa_rain_6h.ncl"

        self.max_forecast_time = f"{get_forecast_hour(self.forecast_timedelta):03}"
        self.min_forecast_time = f"{(get_forecast_hour(self.forecast_timedelta) - 6):03}"
        self.forecast_time_interval = 12

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./Rain_6H_{self.start_time}{forecast_hour}_SWFDP_SA.png"
        }]
