"""
雷达组合反射率

图片样例请访问 NMC 官网：
    http://www.nmc.cn/publish/area/china/radar.html
"""
from sokort.systems.grapes_tym import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "cn_radar_reflectivity"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "plot_radar_reflectivity.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than 0h.")

    def get_image_list(self):
        return [{
            "path": f"GRAPES_MESO-radar-combination-reflectivity-{self.start_time}_{self.forecast_hour}.png"
        }]

    def _check_forecast_time(self) -> bool:
        forecast_hour = int(self.forecast_hour)
        return not forecast_hour == 0
