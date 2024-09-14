from sokort.systems.cma_gfs.graphics.aea_fc import AeaFcPlotter


class Plotter(AeaFcPlotter):
    """
    850hPa 相对涡度

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=0313031602
    """
    plot_types = [
        "cn.vor_850"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AeaFcPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_VOR_P850_FC_AEA.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than 0h.")

    def _check_forecast_time(self) -> bool:
        return not int(self.forecast_hour) == 0
