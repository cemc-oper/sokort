# coding: utf-8

import datetime

import pytimeparse

from nwpc_graphics.systems.grapes_gfs_gmf.plotter import BasePlotter


class AnAeaPlotter(BasePlotter):
    def __init__(self, task: dict, work_dir: str, config: dict):
        BasePlotter.__init__(self, task, work_dir, config)

    def _get_image_list(self):
        forecast_timedelta = datetime.timedelta(
            seconds=pytimeparse.parse(self.task["forecast_time"]))  # datetime.timedelta(hours=3)
        forecast_hour = f"{int(forecast_timedelta.total_seconds()) // 3600:03}"
        return [{
            "path": f"./AEA_AN_{forecast_hour}.png"
        }]
