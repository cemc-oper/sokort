from sokort.systems.grapes_gfs_gmf._plotter import SystemPlotter


class FcAhnePlotter(SystemPlotter):
    def __init__(self, task: dict, work_dir: str, config: dict):
        SystemPlotter.__init__(self, task, work_dir, config)

    def get_image_list(self):
        forecast_hour = f"{int(self.forecast_timedelta.total_seconds()) // 3600:03}"
        return [{
            "path": f"./AHNE_FC_{forecast_hour}.png"
        }]
