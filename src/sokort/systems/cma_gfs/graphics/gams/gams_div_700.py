from sokort.systems.cma_gfs.graphics.gams import GamsPlotter


class Plotter(GamsPlotter):
    """
    700hPa 散度

    图片暂时没有外网访问渠道。
    """
    plot_types = [
        "gams.div_700"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        GamsPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "gams_div_700.ncl"

    def get_image_list(self):
        return [{
            "path": f"./EDI_ASIA_L70_P9_{self.start_time}00{self.forecast_hour}00.png"
        }]
