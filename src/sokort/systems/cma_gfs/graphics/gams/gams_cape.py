"""

"""
from sokort.systems.cma_gfs.graphics.gams import GamsPlotter


class Plotter(GamsPlotter):
    plot_types = [
        "gams.cape"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        GamsPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "gams_cape.ncl"

    def get_image_list(self):
        return [{
            "path": f"./CAPE_ASIA_L88_P9_{self.start_time}00{self.forecast_hour}00.png"
        }]
