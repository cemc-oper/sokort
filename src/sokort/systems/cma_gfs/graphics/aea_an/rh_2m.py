from sokort.systems.cma_gfs.graphics.aea_an import AeaAnPlotter


class Plotter(AeaAnPlotter):
    """
    2m 相对湿度

    003 时效开始

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=03130332
    """
    plot_types = [
        "cn.rh_2m"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AeaAnPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_RH2M_SFC_AN_AEA.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than 0h.")

    def _check_forecast_time(self) -> bool:
        return int(self.forecast_hour) > 0