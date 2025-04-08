from sokort.systems.cma_gfs.graphics.wmc.global_py import WmcGlobalPythonPlotter
from sokort.util import get_forecast_hour


class WmcGlobalPyDiv925Plotter(WmcGlobalPythonPlotter):
    """
    Global, DIV, 925 hPa

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Weather-Models/GRAPES_GFS_new/16a.html
    """
    plot_types = [
        "wmc.global_py.div_925"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(WmcGlobalPyDiv925Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.plot_name = "d925"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_EDI_AGLB_L92_P9_{self.start_time}00{forecast_hour}00.png"
        }]
