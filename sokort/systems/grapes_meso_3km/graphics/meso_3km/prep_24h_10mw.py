"""
24小时降水

图片暂时没有外网访问渠道。
"""
from sokort.systems.grapes_meso_3km.graphics.meso_3km import Meso3kmPlotter


class Plotter(Meso3kmPlotter):
    plot_types = [
        "meso_3km.prep_24h_10mw"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        Meso3kmPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_prep_24hr_10mw.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than 0h.")

    def get_image_list(self):
        return [{
            "path": f"GRAPES-MESOS-prep-{self.start_time}24hr_{self.forecast_hour}_China.png"
        }]

    def _check_forecast_time(self) -> bool:
        forecast_hour = int(self.forecast_hour)
        return (forecast_hour != 0) and (forecast_hour % 24 == 0)
