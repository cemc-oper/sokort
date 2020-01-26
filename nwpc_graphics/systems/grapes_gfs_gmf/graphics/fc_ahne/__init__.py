# coding: utf-8

import datetime

import pytimeparse

from nwpc_graphics.systems.grapes_gfs_gmf.plotter import BasePlotter


class FcAhnePlotter(BasePlotter):
    def __init__(self, task: dict, work_dir: str, config: dict):
        BasePlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = None

    def _get_image_list(self):
        forecast_hour = f"{int(self.forecast_timedelta.total_seconds()) // 3600:03}"
        return [{
            "path": f"./AHNE_FC_{forecast_hour}.png"
        }]
