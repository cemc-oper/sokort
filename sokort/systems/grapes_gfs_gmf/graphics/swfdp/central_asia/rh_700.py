"""
Central Asia, Relative Humidity, 700 hPa

图片样例请访问 NMC 官网：
    http://eng.nmc.cn/ca/publish/up/humidity/700mb.html
"""
from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class CentralAsiaRh700Plotter(SwfdpPlotter):
    plot_types = [
        "swfdp.central_asia.rh_700"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaRh700Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_humidity_700.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./RH_700hPa_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
