"""
Northeast Asia, Wind, 250 hPa

图片样例请访问 WMC-BJ 官网：
    http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES_GFS/Northeast-Asia/Wind/250hPa/index.html
"""
from sokort.systems.grapes_gfs_gmf.graphics.wmc import WmcPlotter
from sokort._util import get_forecast_hour


class NortheastAsiaWind250Plotter(WmcPlotter):
    plot_types = [
        "wmc.northeast_asia.wind_250"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(NortheastAsiaWind250Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "nea_wind_windbarb_250.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_WIND_NEA_L25_P9_{self.start_time}00{forecast_hour}00.png"
        }]
