"""
500 hPa 高度场 + 海平面气压

图片样例请访问 NMC 官网：
    http://www.nmc.cn/publish/area/china/h500p.html
"""
from sokort.systems.grapes_tym import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "cn_500height_mslp"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "plot_height_mslp_500hPa.ncl"

    def get_image_list(self):
        return [{
            "path": f"GRAPES_MESO-500hPa-height-mslp-{self.start_time}_{self.forecast_hour}.png"
        }]
