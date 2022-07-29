from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class SouthAsiaTemp2mPlotter(SwfdpPlotter):
    """
    South Asia, 2m Temperature

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES-GFS-0521/ET0_ASA_L2M_P9.html
    """
    plot_types = [
        "swfdp.south_asia.temp_2m"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthAsiaTemp2mPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sa_temp_2m.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./Temp_2m_{self.start_time}{forecast_hour}_SWFDP_SA.png"
        }]
