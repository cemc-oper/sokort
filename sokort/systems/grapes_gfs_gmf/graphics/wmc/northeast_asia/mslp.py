"""
Northeast Asia, MSLP

图片样例请访问 WMC-BJ 官网：
    http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES_GFS/Northeast-Asia/MSLP/index.html
"""
from sokort.systems.grapes_gfs_gmf.graphics.wmc import WmcPlotter
from sokort._util import get_forecast_hour


class NortheastAsiaMslpPlotter(WmcPlotter):
    plot_types = [
        "wmc.northeast_asia.mslp"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(NortheastAsiaMslpPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "nea_mslp.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_EPH_NEA_L89_P9_{self.start_time}00{forecast_hour}00.png"
        }]
