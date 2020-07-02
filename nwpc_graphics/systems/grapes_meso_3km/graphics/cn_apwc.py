"""
整层可降水量

图片样例请访问 NWPC/CMA 官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=03021509
"""
from nwpc_graphics.systems.grapes_meso_3km import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "cn_apwc"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        SystemPlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "grapes_meso_apwc.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than 0h.")

    def get_image_list(self):
        return [{
            "path": f"GRAPES-MESOS-APWC-{self.start_time}_{self.forecast_hour}_cn.png"
        }]

    def _check_forecast_time(self) -> bool:
        forecast_hour = int(self.forecast_hour)
        return not forecast_hour == 0
