from sokort.systems.cma_tym import SystemPlotter, AREA_LIST


class Plotter(SystemPlotter):
    """
    700 hPa / 850 hPa 水汽通量散度

    图片样例请访问 NWPC/CMA 官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=0302160311
    """
    plot_types = [
        "area_850hPa_qv_div"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "grapes_meso_reg_850hPa_qv_div.ncl"

    def get_image_list(self):
        return [
            {
                "name": area["name"],
                "path": f"GRAPES-MESOS-reg-850hPa-qv-div-{area['image_path_name']}-{self.start_time}_{self.forecast_hour}.png"
            } for area in AREA_LIST
        ]
