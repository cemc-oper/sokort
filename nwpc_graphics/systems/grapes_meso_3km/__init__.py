import pathlib
import datetime

import pandas as pd

from nwpc_graphics.systems.grapes_meso_3km._plotter import SystemPlotter
from nwpc_graphics._logging import get_logger
from nwpc_graphics._util import load_plotters_from_paths
from nwpc_graphics._presenter import Presenter, IPythonPresenter
from nwpc_graphics import get_config


logger = get_logger()


def _load_plotters():
    plotters = load_plotters_from_paths(
        [pathlib.Path(pathlib.Path(__file__).parent, "graphics")],
        SystemPlotter,
    )
    return plotters


plotters = _load_plotters()


def draw_plot(
        plot_type: str,
        start_time: str or datetime.datetime or pd.Timestamp,
        forecast_time: str or pd.Timedelta
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
    plot_module = _get_plotter_class(plot_type)
    if plot_type is None:
        raise ValueError(f"plot type is not supported:{plot_type}")

    if isinstance(start_time, str):
        start_time = pd.to_datetime(start_time, format="%Y%m%d%H")

    if isinstance(forecast_time, str):
        forecast_time = pd.to_timedelta(forecast_time)

    plotter = plot_module.create_plotter(
        graphics_config=get_config(),
        start_time=start_time,
        forecast_time=forecast_time)

    plotter.run_plot()


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
