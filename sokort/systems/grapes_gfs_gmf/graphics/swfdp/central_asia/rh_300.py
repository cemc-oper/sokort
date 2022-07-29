from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class CentralAsiaRh300Plotter(SwfdpPlotter):
    """
    Central Asia, Relative Humidity, 300 hPa

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/humidity/300mb.html
    """
    plot_types = [
        "swfdp.central_asia.rh_300"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaRh300Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_humidity_300.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./RH_300hPa_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
