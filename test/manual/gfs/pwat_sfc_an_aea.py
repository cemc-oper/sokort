# coding: utf-8
import datetime

import click

from nwpc_graphics.systems.grapes_gfs_gmf.pwat_sfc_an_aea import run_plot


@click.command()
@click.option("--work-dir", help="work directory")
def cli(work_dir):
    forecast_data_format = "grib2"
    forecast_data_center = "ecmwf"

    run_plot(
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
    )


if __name__ == "__main__":
    cli()
