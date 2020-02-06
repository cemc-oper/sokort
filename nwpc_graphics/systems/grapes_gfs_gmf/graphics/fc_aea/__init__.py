from nwpc_graphics.systems.grapes_gfs_gmf.plotter import SystemPlotter


class FcAeaPlotter(SystemPlotter):
    def __init__(self, task: dict, work_dir: str, config: dict):
        SystemPlotter.__init__(self, task, work_dir, config)

    def _get_image_list(self):
        forecast_hour = f"{int(self.forecast_timedelta.total_seconds()) // 3600:03}"
        return [{
            "path": f"./AEA_FC_{forecast_hour}.png"
        }]
