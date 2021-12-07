"""
South Asia, Wind (streamline), 500 hPa

图片样例请访问 WMC-BJ 官网：
    http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES-GFS-0521/EWS_ASA_L50_P9.html
"""
from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class SouthAsiaWindSteamline500Plotter(SwfdpPlotter):
    plot_types = [
        "swfdp.south_asia.wind_streamline_500"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthAsiaWindSteamline500Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sa_wind_streamlines_500.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./Wind_Streamlines_500hPa_{self.start_time}{forecast_hour}_SWFDP_SA.png"
        }]
