from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class CentralAsiaRain12Plotter(SwfdpPlotter):
    """
    Central Asia, 12h accumulated precipitation

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/tape12.html
    """
    plot_types = [
        "swfdp.central_asia.rain_12"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaRain12Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_rain12.ncl"

        self.max_forecast_time = f"{get_forecast_hour(self.forecast_timedelta):03}"
        self.min_forecast_time = f"{(get_forecast_hour(self.forecast_timedelta) - 12):03}"
        self.forecast_time_interval = 6

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta)}"

        return [{
            "path": f"./RAIN12_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
