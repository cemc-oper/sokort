from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class SouthAsiaVerticalVelocity850Plotter(SwfdpPlotter):
    """
    South Asia, Vertical Velocity, 850 hPa

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES-GFS-0521/EWP_ASA_L85_P9.html
    """
    plot_types = [
        "swfdp.south_asia.vv_850"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthAsiaVerticalVelocity850Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sa_vv_850.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./VV_850hPa_{self.start_time}{forecast_hour}_SWFDP_SA.png"
        }]
