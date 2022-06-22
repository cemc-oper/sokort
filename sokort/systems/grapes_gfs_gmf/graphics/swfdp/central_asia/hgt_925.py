from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class CentralAsiaHgt925Plotter(SwfdpPlotter):
    """
    Central Asia, geopotential height, 925 hPa

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/geopotential_height/925mb.html
    """
    plot_types = [
        "swfdp.central_asia.hgt_925"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaHgt925Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_hgt_925.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./HGT_925hPa_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
