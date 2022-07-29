from sokort.systems.grapes_gfs_gmf.graphics.swfdp.south_east_asia import SwfdpSeaPlotter
from sokort.util import get_forecast_hour


class SouthEastAsiaTemp700Plotter(SwfdpSeaPlotter):
    """
    South East Asia, Temperature, 700 hPa

    图片样例请访问 NMC 官网：暂缺
    """
    plot_types = [
        "swfdp.south_east_asia.temp_700"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthEastAsiaTemp700Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sea_temp_700hPa.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./TEMP_700hPa_{self.start_time}{forecast_hour}_SWFDP_SEA.png"
        }]
