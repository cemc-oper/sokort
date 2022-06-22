from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class CentralAsiaHgt850Plotter(SwfdpPlotter):
    """
    Central Asia, geopotential height, 850 hPa

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/geopotential_height/850mb.html
    """
    plot_types = [
        "swfdp.central_asia.hgt_850"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaHgt850Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_hgt_850.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./HGT_850hPa_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
