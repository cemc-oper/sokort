"""
South East Asia, Temperature 2M + MSLP

图片样例请访问 NMC 官网：暂缺
"""
from sokort.systems.grapes_gfs_gmf.graphics.swfdp.south_east_asia import SwfdpSeaPlotter
from sokort._util import get_forecast_hour


class SouthEastAsiaTemp2mMslpPlotter(SwfdpSeaPlotter):
    plot_types = [
        "swfdp.south_east_asia.temp_2m_mslp"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthEastAsiaTemp2mMslpPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sea_temp_2m_MSLP.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./TEMP_2m_MSLP_{self.start_time}{forecast_hour}_SWFDP_SEA.png"
        }]
