"""
Central Asia, Relative Humidity, 250 hPa

图片样例请访问 NMC 官网：
    http://eng.nmc.cn/ca/publish/up/humidity/250mb.html
"""
from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class CentralAsiaRh250Plotter(SwfdpPlotter):
    plot_types = [
        "swfdp.central_asia.rh_250"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaRh250Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_humidity_250.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./RH_250hPa_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
