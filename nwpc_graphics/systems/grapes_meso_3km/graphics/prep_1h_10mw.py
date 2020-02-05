from nwpc_graphics.systems.grapes_meso_3km.plotter import BasePlotter


class Plotter(BasePlotter):
    plot_types = [
        "prep_1h_10mw"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        BasePlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "grapes_meso_prep_1hr_10mw.ncl"

    def _get_image_list(self):
        forecast_hour = f"{int(self.forecast_timedelta.total_seconds()) // 3600:03}"
        return [{
            "path": f"GRAPES-MESOS-prep-{self.start_time}1hr_{forecast_hour}_China.png"
        }]
