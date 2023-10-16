from sokort.systems.grapes_gfs_gmf.graphics.wmc import WmcPlotter
from sokort.util import get_forecast_hour


class AfricaDiv700Plotter(WmcPlotter):
    """
    Africa, DIV, 700 hPa

    图片样例请访问 WMC-BJ 官网：暂缺
    """
    plot_types = [
        "wmc.africa.div_700"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(AfricaDiv700Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "africa_div_700.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_EDI_AFRICA_L70_P9_{self.start_time}00{forecast_hour}00.png"
        }]
