from sokort.systems.cma_gfs.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class CentralAsiaWindStreamline200Plotter(SwfdpPlotter):
    """
    Central Asia, wind, streamlines, 200hPa

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/wind/steamlines/200mb3.html
    """
    plot_types = [
        "swfdp.central_asia.wind_streamline_200"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaWindStreamline200Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_wind_streamlines_200.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./WIND_streamlines_200hPa_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
