from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class SouthAsiaRh700Plotter(SwfdpPlotter):
    """
    South Asia, Relative Humidity, 700 hPa

    图片样例请访问 WMC-BJ 官网：暂缺
    """
    plot_types = [
        "swfdp.south_asia.rh_700"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthAsiaRh700Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sa_rh_700.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./RH_700hPa_{self.start_time}{forecast_hour}_SWFDP_SA.png"
        }]
