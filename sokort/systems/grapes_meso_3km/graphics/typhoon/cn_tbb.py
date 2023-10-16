from sokort.systems.grapes_meso_3km.graphics.typhoon import TyphoonPythonPlotter


class Plotter(TyphoonPythonPlotter):
    """
    卫星云图
    """
    plot_types = [
        "typhoon.cn_tbb"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(Plotter, self).__init__(task, work_dir, config, **kwargs)
        self.python_script_name = "meso_plot_tbb.py"

    def get_image_list(self):
        return [
            {
                "path": f"./CMA-MESO.TB.{channel}.{self.start_time}{self.forecast_hour}.png"
            } for channel in ["CH2", "CH4"]
        ]
