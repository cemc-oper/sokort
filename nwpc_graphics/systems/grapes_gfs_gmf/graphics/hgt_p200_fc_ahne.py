# coding: utf-8
#   200hPa高度
#   http://nwpc.nmc.cn/list.jhtml?class_id=031301

import datetime

import pytimeparse

from nwpc_graphics.systems.grapes_gfs_gmf.plotter import BasePlotter


class Plotter(BasePlotter):
    def __init__(self, task: dict, work_dir: str, config: dict):
        BasePlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "GFS_GRAPES_HGT_P200_FC_AHNE.ncl"

    def _get_image_list(self):
        forecast_timedelta = datetime.timedelta(
            seconds=pytimeparse.parse(self.task["forecast_time"]))  # datetime.timedelta(hours=3)
        forecast_hour = f"{int(forecast_timedelta.total_seconds()) // 3600:03}"
        return [{
            "path": f"./AHNE_FC_{forecast_hour}.png"
        }]
