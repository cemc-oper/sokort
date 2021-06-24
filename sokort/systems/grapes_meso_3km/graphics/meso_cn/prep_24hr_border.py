"""
24 小时降水

图片样例请访问 NMC 官网：
    http://www.nmc.cn/publish/area/china/24hrain.html
"""
from sokort.systems.grapes_meso_3km import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "prep_24hr_border"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_prep_24hr_border.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than or equal to 24h.")

    def get_image_list(self):
        return [{
            "path": f"GRAPES-MESOS-prep-{self.start_time}24hr_{self.forecast_hour}_cn.png"
        }]

    def _check_forecast_time(self) -> bool:
        forecast_hour = int(self.forecast_hour)
        return forecast_hour >= 24
