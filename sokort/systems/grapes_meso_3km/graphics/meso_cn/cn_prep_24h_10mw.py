"""
24 小时降水 + 10m 风

暂无官网示例
"""
from sokort.systems.grapes_meso_3km import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "cn_prep_24h_10mw"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_3km_prep_24hr_10mw.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than or equal to 24h.")

    def get_image_list(self):
        return [{
            "path": f"GRAPES_MESO-3KM-prep-{self.start_time}24hr_{self.forecast_hour}_China.png"
        }]

    def _check_forecast_time(self) -> bool:
        forecast_hour = int(self.forecast_hour)
        return forecast_hour >= 24
