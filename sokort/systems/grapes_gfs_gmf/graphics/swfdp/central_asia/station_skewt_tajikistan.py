import shutil

from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class CentralAsiaStationSkewtPlotter(SwfdpPlotter):
    """
    Central Asia, SKEWT, Tajikistan, multi cities

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/Tajikistan/Dehavz.html
    """
    plot_types = [
        "swfdp.central_asia.station.skewt.tajikistan"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaStationSkewtPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.country = "Tajikistan"
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
            "Dangara_38847",
            "Darvoz_38856",
            "Dushanbe_38836",
            "Khorog_38954",
            "Khovaling_38846",
            "Khudjant_38599",
            "Kurgan-Tyube_38933",
            "Lyahsh_38744",
            "Murgab_38878",
            "Rasht_38851",
            "Shaartuz_38937",
            "Dehavz_38734",
            "Iskanderkul_38718",
            "Penjikent_38705",
            "Parkhar_38944",
        ]]
