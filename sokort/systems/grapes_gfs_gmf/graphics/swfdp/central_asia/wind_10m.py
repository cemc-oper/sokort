"""
Central Asia, 10 meters wind

图片样例请访问 NMC 官网：
    http://eng.nmc.cn/ca/publish/up/windL10M.html
"""
from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class CentralAsiaWind10mPlotter(SwfdpPlotter):
    plot_types = [
        "swfdp.central_asia.wind_10m"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaWind10mPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_wind_10m.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./WIND_10M_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
