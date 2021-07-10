"""
0 - 1 km 垂直风切变

图片样例请访问 NWPC/CMA 官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=0302160315
"""
from sokort.systems.grapes_tym import SystemPlotter, AREA_LIST


class Plotter(SystemPlotter):
    plot_types = [
        "area_shr1"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_shr1.ncl"

    def get_image_list(self):
        return [
            {
                "name": area["name"],
                "path": f"GRAPES-MESOS-shr1-{self.start_time}_{self.forecast_hour}_{area['image_path_name']}.png"
            } for area in AREA_LIST
        ]
