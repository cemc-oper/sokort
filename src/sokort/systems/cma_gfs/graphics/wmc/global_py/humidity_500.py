from sokort.systems.cma_gfs.graphics.wmc.global_py import WmcGlobalPythonPlotter
from sokort.util import get_forecast_hour


class WmcHumidity500Plotter(WmcGlobalPythonPlotter):
    """
    Global, Humidity, 500 hPa

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Weather-Models/GRAPES_GFS_new/13.html
    """
    plot_types = [
        "wmc.global_py.humidity_500"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(WmcHumidity500Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.plot_name = "r500"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_ERH_AGLB_L50_P9_{self.start_time}00{forecast_hour}00.png"
        }]
