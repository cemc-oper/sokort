# coding: utf-8
import datetime
import tempfile

from nwpc_graphics.systems.grapes_gfs_gmf import pwat_sfc_an_aea


plot_mapper = {
    "pwat_sfc_an_aea": pwat_sfc_an_aea
}


def draw_plot(plot_type: str, start_date: str, start_time: str, forecast_time: str):
    if plot_type not in plot_mapper:
        raise Exception("plot type is not supported")

    params = _get_params(plot_type, start_date, start_time, forecast_time)

    run_plot = plot_mapper[plot_type].run_plot
    run_plot(**params)


def show_plot(plot_type: str, start_date: str, start_time: str, forecast_time: str):
    if plot_type not in plot_mapper:
        raise Exception("plot type is not supported")

    params = _get_params(plot_type, start_date, start_time, forecast_time)

    run_plot = plot_mapper[plot_type].run_plot
    run_plot(**params)

    graph_show_plot = plot_mapper[plot_type].show_plot
    return graph_show_plot(**params)


def _get_params(plot_type: str, start_date: str, start_time: str, forecast_time: str):
    start_datetime = datetime.datetime.strptime(f"{start_date}{start_time}", "%Y%m%d%H")
    start_datetime_4dvar = start_datetime - datetime.timedelta(hours=3)
    start_time_4dvar = start_datetime_4dvar.strftime("%Y%m%d%H")

    task = {
        "ncl_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script",
        "script_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script",
        "data_path": f"/sstorage1/COMMONDATA/OPER/NWPC/GRAPES_GFS_GMF/Prod-grib/{start_time_4dvar}/ORIG/",
        "start_datetime": start_datetime.isoformat(),
        "forecast_time": forecast_time,
    }
    work_dir = tempfile.mkdtemp()
    config = {
        "ncl_lib": "/home/wangdp/project/graph/ncllib",
        "geodiag_root": "/home/wangdp/project/graph/GEODIAG",
    }

    return {
        "task": task,
        "work_dir": work_dir,
        "config": config,
    }
