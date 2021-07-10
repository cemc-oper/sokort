"""
CAPE + 850 hPa 风场

图片样例请访问 NWPC/CMA 官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=0302160314
"""
import shutil
import os

from sokort.systems.grapes_tym import SystemPlotter, AREA_LIST


class Plotter(SystemPlotter):
    plot_types = [
        "area_cape_850wind"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_cape_850wind.ncl"

    def get_image_list(self):
        return [
            {
                "name": area["name"],
                "path": f"GRAPES-MESOS-cape-{self.start_time}_{self.forecast_hour}_{area['image_path_name']}.png"
            } for area in AREA_LIST
        ]

    def _prepare_environment(self):
        super(Plotter, self)._prepare_environment()

        script_dir = self.task["script_dir"]
        shutil.copy2(f"{script_dir}/grapes_meso_cape_850wind.rgb", "grapes_meso_cape_850wind.rgb")

    def _generate_environ(self):
        envs = super(Plotter, self)._generate_environ()
        envs["NCARG_COLORMAPS"] = os.path.expandvars("${NCARG_ROOT}/lib/ncarg/colormaps:.")
        return envs
