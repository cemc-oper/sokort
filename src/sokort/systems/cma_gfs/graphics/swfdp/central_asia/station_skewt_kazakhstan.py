import shutil

from sokort.systems.cma_gfs.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class CentralAsiaStationSkewtPlotter(SwfdpPlotter):
    """
    Central Asia, SKEWT, Kazakhstan, multi cities

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/Kyrgyzstan/Batken.html
    """
    plot_types = [
        "swfdp.central_asia.station.skewt.kazakhstan"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaStationSkewtPlotter, self).__init__(task, work_dir, config, **kwargs)

        self.country = "Kazakhstan"
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
            "Aktau_38111",
            "Almaty_36870",
            "Astana_35188",
            "Atyrau_35700",
            "Kostanay_28952",
            "Kyzylorda_38062",
            "Pavlodar_36003",
            "Shymkent_38328",
            "Uralsk_35108",
            "Ust-Kamenogorsk_36403",
            "Taraz_38341",
            "Petropavlovsk_28676",
            "Kokshetau_28879",
            "Karaganda_35394",
            "Zhezkazgan_35671",
            "Semey_36177",
            "Aktobe_35229",
            "Taldykorgan_36778",
        ]]
