from sokort.systems.cma_gfs.graphics.swfdp.south_east_asia import SwfdpSeaPlotter
from sokort.util import get_forecast_hour


class SouthEastAsiaWind10mMslpPlotter(SwfdpSeaPlotter):
    """
    South East Asia, Wind 10m + MSLP

    图片样例请访问 NMC 官网：暂缺
    """
    plot_types = [
        "swfdp.south_east_asia.wind_10m_mslp"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthEastAsiaWind10mMslpPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sea_wind_10m_MSLP.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./WIND_10m_MSLP_{self.start_time}{forecast_hour}_SWFDP_SEA.png"
        }]
