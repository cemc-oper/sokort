from sokort.systems.cma_gfs._plotter import SystemNclPlotter
from sokort.util import get_forecast_hour


class AhneFcPlotter(SystemNclPlotter):
    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemNclPlotter.__init__(self, task, work_dir, config, **kwargs)

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"
        return [{
            "path": f"./AHNE_FC_{forecast_hour}.png"
        }]
