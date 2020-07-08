"""
1小时雷达组合反射率

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=050302
"""
from nwpc_graphics.systems.grapes_meso_3km.graphics.meso_3km import Meso3kmPlotter


class Plotter(Meso3kmPlotter):
    plot_types = [
        "meso_3km.diag1_reg_radar"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        Meso3kmPlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "grapes_meso_reg_radar.ncl"

    def get_image_list(self):
        forecast_hour = f"{int(self.forecast_timedelta.total_seconds()) // 3600:03}"
        return [{
            "path": f"GRAPES_MESO-radar-combination-reflectivity-{self.start_time}_{forecast_hour}.png"
        }]
