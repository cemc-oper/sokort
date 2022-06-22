from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class CentralAsiaWindBarb700Plotter(SwfdpPlotter):
    """
    Central Asia, wind, streamlines, speed/direction

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/wind/speed_driection/700mb.html
    """
    plot_types = [
        "swfdp.central_asia.wind_barb_700"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaWindBarb700Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_wind_windbarb_700.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./WIND_barb_700hPa_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
