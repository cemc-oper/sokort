from sokort.systems.cma_gfs.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class CentralAsiaTemp700Plotter(SwfdpPlotter):
    """
    Central Asia, temperature, 700 hPa

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/temperature/700mb.html
    """
    plot_types = [
        "swfdp.central_asia.temp_700"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaTemp700Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_temp_700.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./TEMP_700hPa_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
