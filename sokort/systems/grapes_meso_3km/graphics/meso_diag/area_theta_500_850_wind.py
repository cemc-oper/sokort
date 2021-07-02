"""
500 hPa 与 850 hPa 假相当位温之差 + 850 hPa 风场

图片样例请访问 NWPC/CMA 官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=0302160314
"""
from sokort.systems.grapes_meso_3km import SystemPlotter, AREA_LIST


class Plotter(SystemPlotter):
    plot_types = [
        "area_theta_500_850_wind"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_reg_theta_500_850_wind.ncl"

    def get_image_list(self):
        return [
            {
                "name": area["name"],
                "path": f"GRAPES-MESOS-reg-PTE-500-850-wind-{area['image_path_name']}-{self.start_time}_{self.forecast_hour}.png"
            } for area in AREA_LIST
        ]
