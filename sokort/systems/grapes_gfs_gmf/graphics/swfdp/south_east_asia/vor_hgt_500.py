"""
South East Asia, Vorticity + HGT 500 hPa

图片样例请访问 NMC 官网：暂缺
"""
from sokort.systems.grapes_gfs_gmf.graphics.swfdp.south_east_asia import SwfdpSeaPlotter
from sokort._util import get_forecast_hour


class SouthEastAsiaVorHgt500Plotter(SwfdpSeaPlotter):
    plot_types = [
        "swfdp.south_east_asia.vor_hgt_500"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthEastAsiaVorHgt500Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sea_Vorticity_HGT_500hPa.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./Vorticity_HGT_500hPa_{self.start_time}{forecast_hour}_SWFDP_SEA.png"
        }]
