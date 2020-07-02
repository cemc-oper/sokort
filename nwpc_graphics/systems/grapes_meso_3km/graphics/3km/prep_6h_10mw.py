"""
6小时降水

图片暂时没有外网访问渠道。
"""
from . import GrapesMeso3kmPlotter


class Plotter(GrapesMeso3kmPlotter):
    plot_types = [
        "3km.prep_6h_10mw"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        GrapesMeso3kmPlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "grapes_meso_prep_6hr_10mw.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than 0h.")

    def get_image_list(self):
        return [{
            "path": f"GRAPES-MESOS-prep-{self.start_time}6hr_{self.forecast_hour}_China.png"
        }]

    def _check_forecast_time(self) -> bool:
        forecast_hour = int(self.forecast_hour)
        return (forecast_hour != 0) and (forecast_hour % 6 == 0)
