"""
3h 降水 + 10m 风场

图片样例请访问 NMC 官网：
    http://www.nmc.cn/publish/area/hs/3h10mw.html
"""
from sokort.systems.grapes_meso_3km import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "area_prep_3h_10mw"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_3km_prep_3hr_10mw_region.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than or equal to 3h.")

    def get_image_list(self):
        return [
            {
                "name": "east_china",
                "path": f"GRAPES_MESO-3KM-prep-{self.start_time}3hr_{self.forecast_hour}_EastChina.png"
            },
            {
                "name": "east_north_west",
                "path": f"GRAPES_MESO-3KM-prep-{self.start_time}3hr_{self.forecast_hour}_East_NorthWest.png"
            },
            {
                "name": "east_south_west",
                "path": f"GRAPES_MESO-3KM-prep-{self.start_time}3hr_{self.forecast_hour}_East_SouthWest.png"
            },
            {
                "name": "north_china",
                "path": f"GRAPES_MESO-3KM-prep-{self.start_time}3hr_{self.forecast_hour}_NorthChina.png"
            },
            {
                "name": "north_east",
                "path": f"GRAPES_MESO-3KM-prep-{self.start_time}3hr_{self.forecast_hour}_NorthEast.png"
            },
            {
                "name": "south_china",
                "path": f"GRAPES_MESO-3KM-prep-{self.start_time}3hr_{self.forecast_hour}_SouthChina.png"
            },
            {
                "name": "xi_zang",
                "path": f"GRAPES_MESO-3KM-prep-{self.start_time}3hr_{self.forecast_hour}_XiZang.png"
            },
            {
                "name": "xin_jiang",
                "path": f"GRAPES_MESO-3KM-prep-{self.start_time}3hr_{self.forecast_hour}_XinJiang.png"
            },
            {
                "name": "central_china",
                "path": f"GRAPES_MESO-3KM-prep-{self.start_time}3hr_{self.forecast_hour}_CentralChina.png"
            },
        ]

    def _check_forecast_time(self) -> bool:
        forecast_hour = int(self.forecast_hour)
        return forecast_hour >= 3
