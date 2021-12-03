"""
Africa, HGT, 500 hPa

图片样例请访问 WMC-BJ 官网：
    http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES_EPS/African/500-hgt/index.html
"""
from sokort.systems.grapes_gfs_gmf.graphics.wmc import WmcPlotter
from sokort._util import get_forecast_hour


class WmcAfricaHgt500Plotter(WmcPlotter):
    plot_types = [
        "wmc.africa.hgt_500"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(WmcAfricaHgt500Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "africa_hgt_500.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_EGH_AFRICA_L50_P9_{self.start_time}00{forecast_hour}00.png"
        }]
