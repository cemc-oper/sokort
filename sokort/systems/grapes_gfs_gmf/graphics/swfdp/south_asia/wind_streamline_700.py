from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class SouthAsiaWindSteamline700Plotter(SwfdpPlotter):
    """
    South Asia, Wind (streamline), 700 hPa

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES-GFS-0521/EWS_ASA_L70_P9.html
    """
    plot_types = [
        "swfdp.south_asia.wind_streamline_700"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthAsiaWindSteamline700Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sa_wind_streamlines_700.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./Wind_Streamlines_700hPa_{self.start_time}{forecast_hour}_SWFDP_SA.png"
        }]
