from nwpc_graphics.systems.grapes_meso_3km.plotter import BasePlotter


class Diag1RegRadar(BasePlotter):
    plot_types = [
        "diag1_reg_radar"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        BasePlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "grapes_meso_3km_reg_radar.ncl"

    def _get_image_list(self):
        forecast_hour = f"{int(self.forecast_timedelta.total_seconds()) // 3600:03}"
        return [{
            "path": f"GRAPES_MESO-radar-combination-reflectivity-{self.start_time}_{forecast_hour}.png"
        }]
