"""
500 hPa 高度场 + 850 hPa 风场 + 850 hPa 大风速（大于等于12）

图片样例请访问 NMC 官网：
    http://www.nmc.cn/publish/area/china/hws.html
"""
from nwpc_graphics.systems.grapes_meso_3km import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "cn_500height_850wind"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        SystemPlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "grapes_meso_3km_500_height_850hPa_wind.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than 0h.")

    def get_image_list(self):
        return [{
            "path": f"GRAPES_MESO-3KM-500hPa-height-850hPa-wind-speed-{self.start_time}_{self.forecast_hour}.png"
        }]

    def _check_forecast_time(self) -> bool:
        forecast_hour = int(self.forecast_hour)
        return not forecast_hour == 0
