"""

"""
from sokort.systems.grapes_gfs_gmf.graphics.typhoon import TyphoonPythonPlotter


class Plotter(TyphoonPythonPlotter):
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
                "path": f"./{self.typhoon_area_lower}.TB.{channel}.{self.start_time}{self.forecast_hour}.png"
            } for channel in ["CH2", "CH4"]
        ]
