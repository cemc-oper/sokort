from sokort.systems.cma_gfs.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class SouthAsiaRh925Plotter(SwfdpPlotter):
    """
    South Asia, Relative Humidity, 925 hPa

    图片样例请访问 WMC-BJ 官网：暂缺
    """
    plot_types = [
        "swfdp.south_asia.rh_925"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthAsiaRh925Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sa_rh_925.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./RH_925hPa_{self.start_time}{forecast_hour}_SWFDP_SA.png"
        }]
