from sokort.systems.cma_gfs.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class SouthAsiaLiftedIndexPlotter(SwfdpPlotter):
    """
    South Asia, Lifted index

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES-GFS-0521/ELI_ASA_L85_P9.html
    """
    plot_types = [
        "swfdp.south_asia.lift"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthAsiaLiftedIndexPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sa_lift.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./Lift_{self.start_time}{forecast_hour}_SWFDP_SA.png"
        }]
