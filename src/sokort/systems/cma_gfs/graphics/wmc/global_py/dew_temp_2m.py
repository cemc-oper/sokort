from sokort.systems.cma_gfs.graphics.wmc.global_py import WmcGlobalPythonPlotter
from sokort.util import get_forecast_hour


class Temp2MPlotter(WmcGlobalPythonPlotter):
    """
    Global, 2M Dew Point Temperature
    """
    plot_types = [
        "wmc.global_py.dew_temp_2m"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(Temp2MPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.plot_name = "2d"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_DPT_AGLB_L2M_P9_{self.start_time}00{forecast_hour}00.png"
        }]
