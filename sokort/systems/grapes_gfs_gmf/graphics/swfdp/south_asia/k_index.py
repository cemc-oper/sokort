from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class SouthAsiaKIndexPlotter(SwfdpPlotter):
    """
    South Asia, K Index

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES-GFS-0521/EKI_ASA_L88_P9.html
    """
    plot_types = [
        "swfdp.south_asia.k_index"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthAsiaKIndexPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sa_k_index.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./K_Index_{self.start_time}{forecast_hour}_SWFDP_SA.png"
        }]
