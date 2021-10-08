"""

"""
from sokort.systems.grapes_gfs_gmf.python_plotter import SystemPythonPlotter


class Plotter(SystemPythonPlotter):
    plot_types = [
        "typhoon.tbb"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(Plotter, self).__init__(task, work_dir, config, **kwargs)
        self.typhoon_area = task["typhoon_area"]
        self.typhoon_area_lower = self.typhoon_area.lower()
        self.python_script_name = f"{self.typhoon_area_lower}_plot_tbb.py"

    def get_image_list(self):
        return [
            {
                "path": f"./{self.typhoon_area_lower}.TB.CH2.{self.start_time}{self.forecast_hour}.png"
            },
            {
                "path": f"./{self.typhoon_area_lower}.TB.CH4.{self.start_time}{self.forecast_hour}.png"
            },
        ]
