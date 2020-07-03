"""
500 hPa 与 850 hPa 假相当位温之差 + 850 hPa 风场

图片样例请访问 NWPC/CMA 官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=0302160314
"""
from nwpc_graphics.systems.grapes_meso_3km import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "area_theta_500_850_wind"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        SystemPlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "grapes_meso_reg_theta_500_850_wind.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than or equal to 0h.")

    def get_image_list(self):
        return [
            {
                "name": "east_china",
                "path": f"GRAPES-MESOS-reg-PTE-500-850-wind-EastChina-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "east_north_west",
                "path": f"GRAPES-MESOS-reg-PTE-500-850-wind-East_NorthWest-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "east_south_west",
                "path": f"GRAPES-MESOS-reg-PTE-500-850-wind-East_SouthWest-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "north_china",
                "path": f"GRAPES-MESOS-reg-PTE-500-850-wind-NorthChina-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "north_east",
                "path": f"GRAPES-MESOS-reg-PTE-500-850-wind-NorthEast-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "south_china",
                "path": f"GRAPES-MESOS-reg-PTE-500-850-wind-SouthChina-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "xi_zang",
                "path": f"GRAPES-MESOS-reg-PTE-500-850-wind-XiZang-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "xin_jiang",
                "path": f"GRAPES-MESOS-reg-PTE-500-850-wind-XinJiang-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "central_china",
                "path": f"GRAPES-MESOS-reg-PTE-500-850-wind-CentralChina-{self.start_time}_{self.forecast_hour}.png"
            },
        ]

    def _check_forecast_time(self) -> bool:
        return True
