from sokort.systems.cma_gfs.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class CentralAsiaCinPlotter(SwfdpPlotter):
    """
    Central Asia, Cin

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/Cin.html
    """
    plot_types = [
        "swfdp.central_asia.cin"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaCinPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_cin.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./CIN_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
