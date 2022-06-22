from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class CentralAsiaThicknessPlotter(SwfdpPlotter):
    """
    Central Asia, 1000-500mb Thickness

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/Thickness.html
    """
    plot_types = [
        "swfdp.central_asia.thickness"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaThicknessPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_thickness.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./Thickness_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
