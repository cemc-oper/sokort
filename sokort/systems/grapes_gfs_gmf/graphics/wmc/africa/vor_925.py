from sokort.systems.grapes_gfs_gmf.graphics.wmc import WmcPlotter
from sokort._util import get_forecast_hour


class AfricaVor925Plotter(WmcPlotter):
    """
    Africa, VOR, 925 hPa

    图片样例请访问 WMC-BJ 官网：暂缺
    """
    plot_types = [
        "wmc.africa.vor_925"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(AfricaVor925Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "africa_vor_925.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_ERV_AFRICA_L92_P9_{self.start_time}00{forecast_hour}00.png"
        }]
