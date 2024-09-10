from sokort.systems.cma_gfs.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class SouthAsiaTotalTotalsIndexPlotter(SwfdpPlotter):
    """
    South Asia, Total totals Index

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES-GFS-0521/ETT_ASA_L88_P9.html
    """
    plot_types = [
        "swfdp.south_asia.total_totals"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthAsiaTotalTotalsIndexPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sa_total_totals.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./Total_Totals_{self.start_time}{forecast_hour}_SWFDP_SA.png"
        }]
