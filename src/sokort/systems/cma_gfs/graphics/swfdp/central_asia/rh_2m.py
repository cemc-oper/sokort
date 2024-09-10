from sokort.systems.cma_gfs.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class CentralAsiaRh2mPlotter(SwfdpPlotter):
    """
    Central Asia, Relative Humidity, 2m

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/humidity/2mmb.html
    """
    plot_types = [
        "swfdp.central_asia.rh_2m"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaRh2mPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_rh_2m.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./RH_2M_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
