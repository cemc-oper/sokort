"""
Central Asia, SKEWT, Uzbekistan, multi cities

图片样例请访问 NMC 官网：
    http://eng.nmc.cn/ca/publish/up/Uzbekistan/Buhara.html
"""
import shutil

from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import get_forecast_hour


class CentralAsiaStationSkewtPlotter(SwfdpPlotter):
    plot_types = [
        "swfdp.central_asia.station.skewt.uzbekistan"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaStationSkewtPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.country = "Uzbekistan"
        self.ncl_script_name = f"swfdp_ca_skewT_{self.country}.ncl"

    def _prepare_environment(self):
        super(CentralAsiaStationSkewtPlotter, self)._prepare_environment()

        ncl_dir = self.task["ncl_dir"]

        try:
            shutil.copy2(f"{ncl_dir}/station_{self.country}.txt", f"station_{self.country}.txt")
        except shutil.SameFileError:
            pass

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./SkewT_{station_name}_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        } for station_name in [
            "Buhara_38683",
            "Fergana_38618",
            "Karshi_38812",
            "Nukus_38264",
            "Samarkand_38696",
            "Tashkent_38457",
            "Termez_38927",
            "Navoi_38567",
            "Urgench_38396",
            "Dzizak_38579",
            "Chimgan_38706",
            "Andizan_38475",
            "Uchkuduk_38287",
            "Kamchik_38467",
        ]]
