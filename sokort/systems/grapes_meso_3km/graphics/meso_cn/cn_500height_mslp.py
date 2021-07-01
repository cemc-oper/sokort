"""
500 hPa 高度场 + 海平面气压

图片样例请访问 NMC 官网：
    http://www.nmc.cn/publish/area/china/h500p.html
"""
from sokort.systems.grapes_meso_3km import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "cn_500height_mslp"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_3km_500_height_mslp.ncl"

    def get_image_list(self):
        return [{
            "path": f"GRAPES_MESO-3KM-500hPa-height-mslp-{self.start_time}_{self.forecast_hour}.png"
        }]
