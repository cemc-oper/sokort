"""

"""
from sokort.systems.grapes_gfs_gmf.graphics.typhoon import TyphoonPlotter


class Plotter(TyphoonPlotter):
    plot_types = [
        "typhoon.wind_10m"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(Plotter, self).__init__(task, work_dir, config, **kwargs)
        self.ncl_script_name = f"GFS_GRAPES_WIND_10M_FC_{self.typhoon_area}.ncl"

    def get_image_list(self):
        return [{
            "path": f"./{self.typhoon_area}_FC_{self.forecast_hour}.png"
        }]
