"""
500 hPa 温度和露点差

图片样例请访问 NWPC/CMA 官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=0302160312
"""
from sokort.systems.grapes_meso_3km import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "area_500hPa_temp_dew_temp"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_reg_500hPa_temp_dew_temp.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than or equal to 0h.")

    def get_image_list(self):
        return [
            {
                "name": "east_china",
                "path": f"GRAPES-MESOS-reg-500hPa-temp-dew-temp-diff-EastChina-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "east_north_west",
                "path": f"GRAPES-MESOS-reg-500hPa-temp-dew-temp-diff-East_NorthWest-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "east_south_west",
                "path": f"GRAPES-MESOS-reg-500hPa-temp-dew-temp-diff-East_SouthWest-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "north_china",
                "path": f"GRAPES-MESOS-reg-500hPa-temp-dew-temp-diff-NorthChina-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "north_east",
                "path": f"GRAPES-MESOS-reg-500hPa-temp-dew-temp-diff-NorthEast-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "south_china",
                "path": f"GRAPES-MESOS-reg-500hPa-temp-dew-temp-diff-SouthChina-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "xi_zang",
                "path": f"GRAPES-MESOS-reg-500hPa-temp-dew-temp-diff-XiZang-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "xin_jiang",
                "path": f"GRAPES-MESOS-reg-500hPa-temp-dew-temp-diff-XinJiang-{self.start_time}_{self.forecast_hour}.png"
            },
            {
                "name": "central_china",
                "path": f"GRAPES-MESOS-reg-500hPa-temp-dew-temp-diff-CentralChina-{self.start_time}_{self.forecast_hour}.png"
            },
        ]

    def _check_forecast_time(self) -> bool:
        return True
