from sokort.systems.cma_gfs.graphics.wmc import WmcPlotter
from sokort.util import get_forecast_hour


class WmcHgt500Plotter(WmcPlotter):
    """
    Global, VOR, 925 hPa

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Weather-Models/GRAPES_GFS_new/14b.html
    """
    plot_types = [
        "wmc.global.vor_925"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(WmcHgt500Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "wmc_vor_925.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_ERV_AGLB_L92_P9_{self.start_time}00{forecast_hour}00.png"
        }]
