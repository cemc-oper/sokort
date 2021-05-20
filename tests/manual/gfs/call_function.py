# coding: utf-8
"""
示例命令行程序，展示如何使用nwp_graphics包绘制图像
"""
import datetime

import click

from sokort.systems.grapes_gfs_gmf.graphics.an_aea.pwat_sfc_an_aea import Plotter


@click.command()
@click.option("--work-dir", help="work directory")
def cli(work_dir):
    Plotter(
        task={
            "ncl_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script",
            "script_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script",
            "data_path": "/sstorage1/COMMONDATA/OPER/NWPC/GRAPES_GFS_GMF/Prod-grib/2020011021/ORIG/",
            "start_datetime": datetime.datetime(2020, 1, 11, 0).isoformat(),
            "forecast_time": "24h",
        },
        work_dir=work_dir,
        config={
            "ncl_lib": "/home/wangdp/project/graph/ncllib",
            "geodiag_root": "/home/wangdp/project/graph/GEODIAG",
        }
    ).run_plot()


if __name__ == "__main__":
    cli()
