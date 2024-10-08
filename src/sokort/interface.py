import datetime
import inspect
from typing import Union
from pathlib import Path

import pandas as pd

from ._logging import get_logger, convert_verbose
from .config import get_config
from .util import fix_system_name, parse_start_time, parse_forecast_time
from ._presenter import Presenter, IPythonPresenter


logger = get_logger()


def get_system_module(system: str):
    if system in ("cma_gfs", "cma_gfs_gmf"):
        from sokort.systems import cma_gfs
        return cma_gfs
    elif system in ("cma_meso", "cma_meso_3km", "cma_meso_1km"):
        from sokort.systems import cma_meso
        return cma_meso
    elif system == "cma_tym":
        from sokort.systems import cma_tym
        return cma_tym
    else:
        raise ValueError(f"system is not supported: {system}")


def get_plotter_class(system, plot_type):
    system_module = get_system_module(system)
    return system_module.get_plotter_class(plot_type)


def draw_plot(
        system: str,
        plot_type: str,
        start_time: Union[str, datetime.datetime, pd.Timestamp],
        forecast_time: Union[str, pd.Timedelta] = None,
        data_directory: Union[str, Path] = None,
        work_directory: Union[str, Path] = None,
        verbose: Union[bool, int] = False,
        **kwargs
):
    """Draw images and save them in work directory.

    Parameters
    ----------
    system: str
    plot_type : str
        Plot type according to systems.
    start_time: str or datetime.datetime or pd.Timestamp
        Start time:
            - str: YYYYMMDDHH or other strings supported by ``pandas.to_datetime``
            - ``datetime.datetime`` or ``pd.Timestamp``
    forecast_time: str or pd.Timedelta
        Forecast time duration, such as 3h.
    data_directory:
        Dir for model GIRB2 data.
    work_directory:
        Dir to run plot script.
    verbose:
        print setting

    Raises
    -------
    ValueError
        plot_type is not found
    """
    verbose = convert_verbose(verbose)
    system = fix_system_name(system)

    plotter_class = get_plotter_class(system, plot_type)
    if plotter_class is None:
        raise ValueError(f"plot type is not supported:{plot_type}")

    start_time = parse_start_time(start_time)
    forecast_time = parse_forecast_time(forecast_time)

    plotter = plotter_class.create_plotter(
        system_name=system,
        graphics_config=get_config(),
        start_time=start_time,
        forecast_time=forecast_time,
        data_directory=data_directory,
        work_directory=work_directory,
        verbose=verbose,
        **kwargs,
    )

    plotter.run_plot()

    if verbose >= 1:
        logger.info(f"image list: {plotter.get_image_list()}")


def show_plot(
        system: str,
        plot_type: str,
        start_time: Union[str, datetime.datetime, pd.Timestamp],
        forecast_time: Union[str, pd.Timedelta],
        presenter: Presenter = IPythonPresenter(),
        data_directory: Union[str, Path] = None,
        work_directory: Union[str, Path] = None,
        verbose: Union[bool, int] = False,
        **kwargs
):
    """
    Draw images and show them in Jupyter Notebook.

    Parameters
    ----------
    system:
    plot_type : str
        Plot type according to systems.
    start_time: str or datetime.datetime or pd.Timestamp
        Start time:
            - str: YYYYMMDDHH, or other time strings (supported by ``pd.to_datetime``)
            - datetime.datetime or pd.Timestamp
    forecast_time: str or pd.Timedelta
        Forecast time duration, such as 3h.
    presenter: Presenter
        image presenter
    data_directory
    work_directory
    verbose

    Raises
    -------
    ValueError
        plot_type is not found
    """
    verbose = convert_verbose(verbose)
    system = fix_system_name(system)

    plotter_class = get_plotter_class(system, plot_type)
    if plotter_class is None:
        raise ValueError(f"plot type is not supported:{plot_type}")

    start_time = parse_start_time(start_time)
    forecast_time = parse_forecast_time(forecast_time)

    plotter = plotter_class.create_plotter(
        graphics_config=get_config(),
        start_time=start_time,
        forecast_time=forecast_time,
        data_directory=data_directory,
        work_directory=work_directory,
        verbose=verbose,
        **kwargs
    )

    plotter.run_plot()

    presenter.show_plot(plotter.get_image_list())


def list_plot_type(
        system: str,
        with_summary: bool = True,
):
    system = fix_system_name(system)
    system_module = get_system_module(system)

    plotters = system_module.plotters
    for key, some_plotter in plotters.items():
        docs = some_plotter.__doc__
        if docs is None:
            plotter_summary = None
        else:
            docs = inspect.cleandoc(docs)
            plotter_summary = docs.splitlines()[0]
        if plotter_summary is None:
            print(key)
        else:
            print(f"{key} : {plotter_summary}")
