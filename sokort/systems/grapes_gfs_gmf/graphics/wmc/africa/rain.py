"""
Africa, Precipitation

图片样例请访问 WMC-BJ 官网：
    http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES_EPS/African/6xiaoshileijijiangshui/index.html
"""
from sokort.systems.grapes_gfs_gmf.graphics.wmc import WmcPlotter
from sokort._util import get_forecast_hour


class AfricaRainPlotter(WmcPlotter):
    plot_types = [
        "wmc.africa.rain"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(AfricaRainPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "africa_rain.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_RAIN_AFRICA_L88_P9_{self.start_time}00{forecast_hour}00.png"
        }]
