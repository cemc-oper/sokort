# coding: utf-8
import datetime
import tempfile
import importlib
import pathlib

from nwpc_graphics.systems.grapes_gfs_gmf import plotter
from nwpc_graphics.logging import get_logger
from nwpc_graphics.systems.grapes_gfs_gmf.util import load_plotters_from_paths


logger = get_logger()


def _load_plotters():
    plotters = load_plotters_from_paths([pathlib.Path(pathlib.Path(__file__).parent, "graphics")])
    return plotters


plotters = _load_plotters()


def draw_plot(plot_type: str, start_date: str, start_time: str, forecast_time: str):
    """Draw images and save them in work directory.

    Parameters
    ----------
    plot_type : str
        Plot type according to systems.
    start_date: str
        Start date, YYYYMMDD
    start_time: str
        Start hour, HH
    forecast_time: str
        Forecast time duration, such as 3h.

    Raises
    -------
    ValueError
        plot_type is not found
    """
    plot_module = _get_plot_module(plot_type)
    if plot_type is None:
        raise ValueError(f"plot type is not supported:{plot_type}")

    params = _get_params(plot_type, start_date, start_time, forecast_time)

    p = plot_module.Plotter
    p(**params).run_plot()


def show_plot(plot_type: str, start_date: str, start_time: str, forecast_time: str):
    """Draw images and show them in Jupyter Notebook.

    Parameters
    ----------
    plot_type : str
        Plot type according to systems.
    start_date: str
        Start date, YYYYMMDD
    start_time: str
        Start hour, HH
    forecast_time: str
        Forecast time duration, such as 3h.

    Raises
    -------
    ValueError
        plot_type is not found
    """
    plot_module = _get_plot_module(plot_type)
    if plot_type is None:
        raise ValueError(f"plot type is not supported:{plot_type}")

    params = _get_params(plot_type, start_date, start_time, forecast_time)

    p = plot_module.Plotter(**params)
    p.run_plot()

    return p.show_plot()


def _get_params(plot_type: str, start_date: str, start_time: str, forecast_time: str):
    """Get params for run_plot method of BasePlotter classes.

    Parameters
    ----------
    plot_type : str
        Plot type according to systems.
    start_date: str
        Start date, YYYYMMDD
    start_time: str
        Start hour, HH
    forecast_time: str
        Forecast time duration, such as 3h.

    Returns
    -------
    dict
        params directory for BasePlotter.run_plot method.
    """
    start_datetime = datetime.datetime.strptime(f"{start_date}{start_time}", "%Y%m%d%H")
    start_datetime_4dvar = start_datetime - datetime.timedelta(hours=3)
    start_time_4dvar = start_datetime_4dvar.strftime("%Y%m%d%H")

    task = {
        "ncl_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script/",
        "script_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script/",
        "data_path": f"/sstorage1/COMMONDATA/OPER/NWPC/GRAPES_GFS_GMF/Prod-grib/{start_time_4dvar}/ORIG/",
        "start_datetime": start_datetime.isoformat(),
        "forecast_time": forecast_time,
    }
    work_dir = tempfile.mkdtemp()
    config = {
        "ncl_lib": "/home/wangdp/project/graph/ncllib/",
        "geodiag_root": "/home/wangdp/project/graph/GEODIAG/",
    }

    return {
        "task": task,
        "work_dir": work_dir,
        "config": config,
    }


def _get_plot_module(plot_type: str):
    """Get plot module

    Parameters
    ----------
    plot_type : str
        Plot type according to systems.

    Returns
    -------
    module or None
        plotter module, return None if not found.
    """
    if plot_type in plotters:
        return plotters[plot_type]
    else:
        return None
