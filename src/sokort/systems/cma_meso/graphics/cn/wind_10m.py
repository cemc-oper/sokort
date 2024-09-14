from sokort.systems.cma_meso import SystemPlotter


class Plotter(SystemPlotter):
    """
    10m 风

    图片样例请访问 NMC 官网：
        http://www.nmc.cn/publish/area/china/10mws.html
    """
    plot_types = [
        "cn.wind_10m"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_3km_10m_wind.ncl"

    def get_image_list(self):
        return [{
            "path": f"GRAPES_MESO-3KM-10m-wind-{self.start_time}_{self.forecast_hour}.png"
        }]
