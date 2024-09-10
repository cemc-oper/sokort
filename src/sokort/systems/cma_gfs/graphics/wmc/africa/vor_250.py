from sokort.systems.cma_gfs.graphics.wmc import WmcPlotter
from sokort.util import get_forecast_hour


class AfricaVor250Plotter(WmcPlotter):
    """
    Africa, VOR, 250 hPa

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES_EPS/African/250xuandu/index.html
    """
    plot_types = [
        "wmc.africa.vor_250"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(AfricaVor250Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "africa_vor_250.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_ERV_AFRICA_L25_P9_{self.start_time}00{forecast_hour}00.png"
        }]
