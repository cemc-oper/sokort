import pathlib
import datetime
from typing import Union, List, Type, Dict

import pandas as pd

from sokort.systems.grapes_meso_3km._plotter import SystemPlotter
from sokort._logging import get_logger
from sokort._util import load_plotters_from_paths
from sokort._presenter import Presenter, IPythonPresenter
from sokort import get_config


logger = get_logger()


def _load_plotters() -> Dict[str, Type[SystemPlotter]]:
    """
    Load plotter in graphics directory.
    """
    p = load_plotters_from_paths(
        [pathlib.Path(pathlib.Path(__file__).parent, "graphics")],
        SystemPlotter,
    )
    return p


plotters = _load_plotters()


def draw_plot(
        plot_type: str,
        start_time: Union[str, datetime.datetime, pd.Timestamp],
        forecast_time: Union[str, pd.Timedelta]
):
    """
    Draw images and save them in work directory.

    Parameters
    ----------
    plot_type : str
        Plot type according to systems.
    start_time: str or datetime.datetime or pd.Timestamp
        Start time:
            - str: YYYYMMDDHH, or other time strings (supported by ``pd.to_datetime``)
            - datetime.datetime
            - pd.Timestamp
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
        if len(start_time) == 10:
            start_time = pd.to_datetime(start_time, format="%Y%m%d%H")
        else:
            start_time = pd.to_datetime(start_time)

    if isinstance(forecast_time, str):
        forecast_time = pd.to_timedelta(forecast_time)

    plotter = plot_module.create_plotter(
        graphics_config=get_config(),
        start_time=start_time,
        forecast_time=forecast_time)

    plotter.run_plot()


def show_plot(
        plot_type: str,
        start_time: Union[str, datetime.datetime, pd.Timestamp],
        forecast_time: Union[str, pd.Timedelta],
        presenter: Presenter = IPythonPresenter(),
):
    """
    Draw images and show them in Jupyter Notebook.

    Parameters
    ----------
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

    Raises
    -------
    ValueError
        plot_type is not found
    """
    plotter_class = _get_plotter_class(plot_type)
    if plotter_class is None:
        raise ValueError(f"plot type is not supported:{plot_type}")

    if isinstance(start_time, str):
        if len(start_time) == 10:
            start_time = pd.to_datetime(start_time, format="%Y%m%d%H")
        else:
            start_time = pd.to_datetime(start_time)

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


def _get_plotter_class(plot_type: str) -> Type[SystemPlotter]:
    """
    Get plot module.

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
