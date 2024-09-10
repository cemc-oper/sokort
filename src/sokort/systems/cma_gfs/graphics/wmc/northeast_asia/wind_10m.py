from sokort.systems.cma_gfs.graphics.wmc import WmcPlotter
from sokort.util import get_forecast_hour


class NortheastAsiaWind10MPlotter(WmcPlotter):
    """
    Northeast Asia, Wind, 10M Wind

    图片样例请访问 WMC-BJ 官网：暂缺
    """
    plot_types = [
        "wmc.northeast_asia.wind_10m"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(NortheastAsiaWind10MPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "nea_wind_10m.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_WIND_NEA_L10M_P9_{self.start_time}00{forecast_hour}00.png"
        }]
