"""
Central Asia, vertical velocity, 500 hPa

图片样例请访问 NMC 官网：
    http://eng.nmc.cn/ca/publish/up/vertical_velocity/500mb.html
"""
from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class CentralAsiaW500Plotter(SwfdpPlotter):
    plot_types = [
        "swfdp.central_asia.w_500"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaW500Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_w_500.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./W_p500_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
