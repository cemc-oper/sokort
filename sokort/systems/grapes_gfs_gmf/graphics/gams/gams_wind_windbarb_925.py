"""
925hPa 风场

图片暂时没有外网访问渠道。
"""
from sokort.systems.grapes_gfs_gmf.graphics.gams import GamsPlotter


class Plotter(GamsPlotter):
    plot_types = [
        "gams.wind_windbarb_925"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        GamsPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "gams_wind_windbarb_925.ncl"

    def get_image_list(self):
        return [{
            "path": f"./EDA_ASIA_L92_P9_{self.start_time}00{self.forecast_hour}00.png"
        }]
