"""
2m 最高温度

图片样例请访问 NMC 官网：
    http://www.nmc.cn/publish/nwpc/grapes_gfs/ea/wind/T2mMax.htm

Notes
-----
需要对原始预报数据进行加工，本库暂时不包括该数据处理程序
"""
from sokort.systems.grapes_gfs_gmf.graphics.t2m_extrems import T2MExtremsPlotter


class Plotter(T2MExtremsPlotter):
    plot_types = [
        "t2m_extrems.max_sfc_an_aea"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        T2MExtremsPlotter.__init__(self, task, work_dir, config, **kwargs)
        self.ncl_script_name = "GFS_GRAPES_T2MMAX_SFC_AN_AEA.ncl"

    def get_image_list(self):
        hour_list = range(24, 121, 24)
        return [{
            "path": f"./GRAPES_GFS-{hour-24:02}-{hour:02}h-2m-max-temp-{self.start_time}.png"
        } for hour in hour_list]
