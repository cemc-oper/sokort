"""
0 - 3 km 垂直风切变

图片样例请访问 NWPC/CMA 官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=0302160316
"""
from sokort.systems.grapes_meso_3km import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "area_shr3"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_shr3.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than or equal to 0h.")

    def get_image_list(self):
        return [
            {
                "name": "east_china",
                "path": f"GRAPES-MESOS-shr3-{self.start_time}_{self.forecast_hour}_EastChina.png"
            },
            {
                "name": "east_north_west",
                "path": f"GRAPES-MESOS-shr3-{self.start_time}_{self.forecast_hour}_East_NorthWest.png"
            },
            {
                "name": "east_south_west",
                "path": f"GRAPES-MESOS-shr3-{self.start_time}_{self.forecast_hour}_East_SouthWest.png"
            },
            {
                "name": "north_china",
                "path": f"GRAPES-MESOS-shr3-{self.start_time}_{self.forecast_hour}_NorthChina.png"
            },
            {
                "name": "north_east",
                "path": f"GRAPES-MESOS-shr3-{self.start_time}_{self.forecast_hour}_NorthEast.png"
            },
            {
                "name": "south_china",
                "path": f"GRAPES-MESOS-shr3-{self.start_time}_{self.forecast_hour}_SouthChina.png"
            },
            {
                "name": "xi_zang",
                "path": f"GRAPES-MESOS-shr3-{self.start_time}_{self.forecast_hour}_XiZang.png"
            },
            {
                "name": "xin_jiang",
                "path": f"GRAPES-MESOS-shr3-{self.start_time}_{self.forecast_hour}_XinJiang.png"
            },
            {
                "name": "central_china",
                "path": f"GRAPES-MESOS-shr3-{self.start_time}_{self.forecast_hour}_CentralChina.png"
            },
        ]

    def _check_forecast_time(self) -> bool:
        return True
