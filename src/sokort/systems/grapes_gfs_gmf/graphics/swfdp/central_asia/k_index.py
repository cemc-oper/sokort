from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class CentralAsiaKIndexPlotter(SwfdpPlotter):
    """
    Central Asia, K_index

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/index.html
    """
    plot_types = [
        "swfdp.central_asia.k_index"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaKIndexPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_k_index.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./K_index_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
