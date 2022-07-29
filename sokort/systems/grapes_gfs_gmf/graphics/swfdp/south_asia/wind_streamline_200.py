from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class SouthAsiaWindSteamline200Plotter(SwfdpPlotter):
    """
    South Asia, Wind (streamline), 200 hPa

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES-GFS-0521/EWS_ASA_L20_P9.html
    """
    plot_types = [
        "swfdp.south_asia.wind_streamline_200"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthAsiaWindSteamline200Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sa_wind_streamlines_200.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./Wind_Streamlines_200hPa_{self.start_time}{forecast_hour}_SWFDP_SA.png"
        }]
