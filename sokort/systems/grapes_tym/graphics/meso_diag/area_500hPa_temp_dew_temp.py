"""
500 hPa 温度和露点差

图片样例请访问 NWPC/CMA 官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=0302160312
"""
from sokort.systems.grapes_tym import SystemPlotter, AREA_LIST


class Plotter(SystemPlotter):
    plot_types = [
        "area_500hPa_temp_dew_temp"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_reg_500hPa_temp_dew_temp.ncl"

    def get_image_list(self):
        return [
            {
                "name": area["name"],
                "path": f"GRAPES-MESOS-reg-500hPa-temp-dew-temp-diff-{area['image_path_name']}-{self.start_time}_{self.forecast_hour}.png"
            } for area in AREA_LIST
        ]
