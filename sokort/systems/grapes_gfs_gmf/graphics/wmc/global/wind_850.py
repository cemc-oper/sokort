"""
Global, Wind, 850 hPa

图片样例请访问 WMC-BJ 官网：
    http://www.wmc-bj.net/publish/Weather-Models/GRAPES_GFS_new/8.html
"""
from sokort.systems.grapes_gfs_gmf.graphics.wmc import WmcPlotter
from sokort._util import get_forecast_hour


class Temp2MPlotter(WmcPlotter):
    plot_types = [
        "wmc.global.wind_850"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(Temp2MPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "wmc_wind_windbarb_850.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_WIND_AGLB_L85_P9_{self.start_time}00{forecast_hour}00.png"
        }]
