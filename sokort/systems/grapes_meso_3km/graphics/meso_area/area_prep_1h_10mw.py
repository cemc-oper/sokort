"""
1h 降水 + 10m 风场

图片样例请访问 NMC 官网：
    http://www.nmc.cn/publish/area/hs/1h10mw.html
"""
from sokort.systems.grapes_meso_3km import SystemPlotter, AREA_LIST


class Plotter(SystemPlotter):
    plot_types = [
        "area_prep_1h_10mw"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_3km_prep_1hr_10mw_region.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than or equal to 1h.")

    def get_image_list(self):
        return [
            {
                "name": area["name"],
                "path": f"GRAPES_MESO-3KM-prep-{self.start_time}1hr_{self.forecast_hour}_{area['image_path_name']}.png"
            } for area in AREA_LIST
        ]

    def _check_forecast_time(self) -> bool:
        forecast_hour = int(self.forecast_hour)
        return forecast_hour >= 1
