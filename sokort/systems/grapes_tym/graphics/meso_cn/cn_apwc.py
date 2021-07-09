"""
整层可降水量

图片样例请访问 NWPC/CMA 官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=03021509
"""
from sokort.systems.grapes_tym import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "cn_apwc"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_apwc.ncl"

    def get_image_list(self):
        return [{
            "path": f"GRAPES-MESOS-APWC-{self.start_time}_{self.forecast_hour}_cn.png"
        }]
