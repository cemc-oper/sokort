from sokort.systems.cma_gfs.graphics.wmc import WmcPlotter
from sokort.util import get_forecast_hour


class AfricaWind500Plotter(WmcPlotter):
    """
    Africa, Wind, 500 hPa

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES_EPS/African/500feng/index.html
    """
    plot_types = [
        "wmc.africa.wind_500"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(AfricaWind500Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "africa_wind_windbarb_500.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_WIND_AFRICA_L50_P9_{self.start_time}00{forecast_hour}00.png"
        }]
