from sokort.systems.grapes_gfs_gmf.graphics.swfdp.south_east_asia import SwfdpSeaPlotter
from sokort.util import get_forecast_hour


class SouthEastAsiaRh2mWind10mMslpPlotter(SwfdpSeaPlotter):
    """
    South East Asia, RH 2M + Wind 10m + MSLP

    图片样例请访问 NMC 官网：暂缺
    """
    plot_types = [
        "swfdp.south_east_asia.rh_2m_wind_10m_mslp"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthEastAsiaRh2mWind10mMslpPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sea_RH_2m_wind_10m_MSLP.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./RH_2m_WIND_10m_MSLP_{self.start_time}{forecast_hour}_SWFDP_SEA.png"
        }]
