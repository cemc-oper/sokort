from sokort.systems.cma_gfs.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class CentralAsiaWindBarb250Plotter(SwfdpPlotter):
    """
    Central Asia, wind, speed/direction, 250hPa

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/wind/speed_driection/250mb.html
    """
    plot_types = [
        "swfdp.central_asia.wind_barb_250"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaWindBarb250Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_wind_windbarb_250.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./WIND_barb_250hPa_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
