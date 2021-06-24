"""
雷达组合反射率

图片样例请访问 NMC 官网：
    http://www.nmc.cn/publish/area/hs/radar.html
"""
from sokort.systems.grapes_meso_3km import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "area_radar_reflectivity"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_3km_radar_region.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than or equal to 0h.")

    def get_image_list(self):
        return [
            {
                "name": "east_china",
                "path": f"GRAPES_MESO-3KM-radar-_EastChina{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "east_north_west",
                "path": f"GRAPES_MESO-3KM-radar-_East_NorthWest{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "east_south_west",
                "path": f"GRAPES_MESO-3KM-radar-_East_SouthWest{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "north_china",
                "path": f"GRAPES_MESO-3KM-radar-_NorthChina{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "north_east",
                "path": f"GRAPES_MESO-3KM-radar-_NorthEast{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "south_china",
                "path": f"GRAPES_MESO-3KM-radar-_SouthChina{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "xi_zang",
                "path": f"GRAPES_MESO-3KM-radar-_XiZang{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "xin_jiang",
                "path": f"GRAPES_MESO-3KM-radar-_XinJiang{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "central_china",
                "path": f"GRAPES_MESO-3KM-radar-_CentralChina{self.start_time}_{self.forecast_hour}.png"
            },
        ]

    def _check_forecast_time(self) -> bool:
        return True
