from sokort.systems.cma_meso import SystemPlotter, AREA_LIST


class Plotter(SystemPlotter):
    """
    0 - 3 km 垂直风切变

    图片样例请访问 NWPC/CMA 官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=0302160316
    """
    plot_types = [
        "area.shr_3km"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_shr3.ncl"

    def get_image_list(self):
        return [
            {
                "name": area["name"],
                "path": f"GRAPES-MESOS-shr3-{self.start_time}_{self.forecast_hour}_{area['image_path_name']}.png"
            } for area in AREA_LIST
        ]
