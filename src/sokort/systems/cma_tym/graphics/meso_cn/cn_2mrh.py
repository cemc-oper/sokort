from sokort.systems.cma_tym import SystemPlotter


class Plotter(SystemPlotter):
    """
    2m 相对湿度

    图片样例请访问 NMC 官网：
    """
    plot_types = [
        "cn_2mrh"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_2m_rh.ncl"

    def get_image_list(self):
        return [{
            "path": f"GRAPES_MESO-2m-relative-humidity-{self.start_time}_{self.forecast_hour}.png"
        }]
