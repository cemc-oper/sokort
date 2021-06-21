import pathlib
import datetime
from typing import Union, Dict

import pandas as pd

from sokort.systems.grapes_gfs_gmf._plotter import SystemPlotter
from sokort._logging import get_logger, convert_verbose
from sokort._util import load_plotters_from_paths
from sokort._presenter import Presenter, IPythonPresenter
from sokort import get_config


logger = get_logger()


def _load_plotters():
    _plotters = load_plotters_from_paths(
        [pathlib.Path(pathlib.Path(__file__).parent, "graphics")],
        SystemPlotter,
    )
    return _plotters


plotters = _load_plotters()


def draw_plot(
        plot_type: str,
        start_time: Union[str, datetime.datetime, pd.Timestamp],
        forecast_time: Union[str, pd.Timedelta],
        verbose: Union[bool, int] = False
):
    """Draw images and save them in work directory.

    Parameters
    ----------
    plot_type : str
        Plot type according to systems.
    start_time: str or datetime.datetime or pd.Timestamp
        Start time:
            - str: YYYYMMDDHH
            - datetime.datetime or pd.Timestamp
    forecast_time: str or pd.Timedelta
        Forecast time duration, such as 3h.

    Raises
    -------
    ValueError
        plot_type is not found
    """
    verbose = convert_verbose(verbose)

    plotter_class = _get_plotter_class(plot_type)
    if plotter_class is None:
        raise ValueError(f"plot type is not supported:{plot_type}")

    if isinstance(start_time, str):
        start_time = pd.to_datetime(start_time, format="%Y%m%d%H")

    if isinstance(forecast_time, str):
        forecast_time = pd.to_timedelta(forecast_time)

    plotter = plotter_class.create_plotter(
        graphics_config=get_config(),
        start_time=start_time,
        forecast_time=forecast_time,
        verbose=verbose
    )

    plotter.run_plot()

    if verbose >= 1:
        logger.info(f"image list: {plotter.get_image_list()}")


def show_plot(
        plot_type: str,
        start_time: str or datetime.datetime or pd.Timestamp,
        forecast_time: str or pd.Timedelta,
        presenter: Presenter = IPythonPresenter(),
):
    """Draw images and show them in Jupyter Notebook.

    Parameters
    ----------
    plot_type : str
        Plot type according to systems.
    start_time: str or datetime.datetime or pd.Timestamp
        Start time:
            - str: YYYYMMDDHH
            - datetime.datetime or pd.Timestamp
    forecast_time: str or pd.Timedelta
        Forecast time duration, such as 3h.
    presenter: Presenter
        image presenter

    Raises
    -------
    ValueError
        plot_type is not found
    """
    plotter_class = _get_plotter_class(plot_type)
    if plotter_class is None:
        raise ValueError(f"plot type is not supported:{plot_type}")

    if isinstance(start_time, str):
        start_time = pd.to_datetime(start_time, format="%Y%m%d%H")

    if isinstance(forecast_time, str):
        forecast_time = pd.to_timedelta(forecast_time)

    plotter = plotter_class.create_plotter(
        graphics_config=get_config(),
        start_time=start_time,
        forecast_time=forecast_time
    )

    plotter.run_plot()

    presenter.show_plot(plotter.get_image_list())

    return


def _get_plotter_class(plot_type: str):
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
