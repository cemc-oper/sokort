"""

"""
from sokort.systems.grapes_gfs_gmf.graphics.typhoon import TyphoonPlotter
from sokort._util import get_forecast_hour


class Plotter(TyphoonPlotter):
    plot_types = [
        "typhoon.rain24_sfc"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(Plotter, self).__init__(task, work_dir, config, **kwargs)
        self.ncl_script_name = f"GFS_GRAPES_RAIN24_SFC_FC_{self.typhoon_area}.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than 24h.")

        forecast_hour = get_forecast_hour(self.forecast_timedelta)
        self.min_forecast_time = f"{forecast_hour - 24:03}"
        self.max_forecast_time = f"{forecast_hour:03}"
        self.forecast_time_interval = 24

    def get_image_list(self):
        return [{
            "path": f"./{self.typhoon_area}_FC_{self.forecast_hour}.png"
        }]

    def _check_forecast_time(self) -> bool:
        forecast_hour = get_forecast_hour(self.forecast_timedelta)
        return forecast_hour >= 24
