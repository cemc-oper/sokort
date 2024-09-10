from sokort.systems.cma_gfs.graphics.wmc import WmcPlotter
from sokort.util import get_forecast_hour


class AfricaTemp250Plotter(WmcPlotter):
    """
    Africa, Temperature, 250 hPa

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES_EPS/African/250wendu/index.html
    """
    plot_types = [
        "wmc.africa.temp_250"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(AfricaTemp250Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "africa_temp_250.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_TMP_AFRICA_L25_P9_{self.start_time}00{forecast_hour}00.png"
        }]
