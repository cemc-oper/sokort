"""
"""
from sokort.systems.grapes_tym import SystemPlotter, AREA_LIST


class Plotter(SystemPlotter):
    plot_types = [
        "area_conv_prep"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_conv_prep.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than or equal to 3h.")

    def get_image_list(self):
        return [
            {
                "name": area["name"],
                "path": f"GRAPES-MESOS-covprep-{self.start_time}3hr_{self.forecast_hour}_{area['image_path_name']}.png"
            } for area in AREA_LIST
        ]

    def _check_forecast_time(self) -> bool:
        forecast_hour = int(self.forecast_hour)
        return forecast_hour >= 3
