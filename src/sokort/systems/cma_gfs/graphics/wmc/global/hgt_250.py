from sokort.systems.cma_gfs.graphics.wmc import WmcPlotter
from sokort.util import get_forecast_hour


class WmcHgt500Plotter(WmcPlotter):
    """
    Global, Geopotential Height, 250 hPa

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Weather-Models/GRAPES_GFS_new/3.html
    """
    plot_types = [
        "wmc.global.hgt_250"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(WmcHgt500Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "wmc_hgt_250.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_EGH_AGLB_L25_P9_{self.start_time}00{forecast_hour}00.png"
        }]
