"""
雷达组合反射率

图片样例请访问 NMC 官网：
    http://www.nmc.cn/publish/area/hs/radar.html
"""
from sokort.systems.grapes_meso_3km import SystemPlotter, AREA_LIST


class Plotter(SystemPlotter):
    plot_types = [
        "area_radar_reflectivity"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_3km_radar_region.ncl"

    def get_image_list(self):
        return [
            {
                "name": area["name"],
                "path": f"GRAPES_MESO-3KM-radar-_{area['image_path_name']}{self.start_time}_{self.forecast_hour}.png"
            } for area in AREA_LIST
        ]
