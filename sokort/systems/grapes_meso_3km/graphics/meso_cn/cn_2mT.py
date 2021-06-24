"""
2m 温度

图片样例请访问 NMC 官网：
    http://www.nmc.cn/publish/shuzhiyubao/GRAPESquyumoshi/quanguo/2mwendu/index.html
"""
from sokort.systems.grapes_meso_3km import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "cn_2mT"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_3km_2m_temp.ncl"

    def get_image_list(self):
        return [{
            "path": f"GRAPES_MESO-3KM-2m-temperature-{self.start_time}_{self.forecast_hour}.png"
        }]
