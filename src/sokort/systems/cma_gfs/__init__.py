import pathlib
import datetime
from typing import Union, Dict, Optional, Type

import pandas as pd

from sokort.systems.cma_gfs._plotter import SystemNclPlotter
from sokort.systems.cma_gfs.graphics.typhoon import TyphoonPythonPlotter
from sokort.systems.cma_gfs.graphics.wmc.global_py import WmcGlobalPythonPlotter
from sokort._plotter import BasePlotter
from sokort._loader import load_plotters_from_paths
from sokort._presenter import Presenter, IPythonPresenter


SYSTEM_NAME = "cma_gfs"


def _load_plotters() -> Dict[str, Type[BasePlotter]]:
    _plotters = load_plotters_from_paths(
        [pathlib.Path(pathlib.Path(__file__).parent, "graphics")],
        (SystemNclPlotter, TyphoonPythonPlotter, WmcGlobalPythonPlotter),
    )
    return _plotters


plotters = _load_plotters()


def draw_plot(
        plot_type: str,
        start_time: Union[str, datetime.datetime, pd.Timestamp],
        forecast_time: Union[str, pd.Timedelta],
        system_name: str = SYSTEM_NAME,
        verbose: Union[bool, int] = False
):
    """Draw images and save them in work directory.

    Parameters
    ----------
    plot_type : str
        Plot type according to systems.
    start_time: str or datetime.datetime or pd.Timestamp
        Start time:
            - str: YYYYMMDDHH or other strings supported by ``pandas.to_datetime``
            - ``datetime.datetime`` or ``pd.Timestamp``
    forecast_time: str or pd.Timedelta
        Forecast time duration, such as 3h.
    system_name
    verbose:
        print setting

    Raises
    -------
    ValueError
        plot_type is not found
    """
    from sokort.interface import draw_plot as base_draw_plot
    return base_draw_plot(
        system=system_name,
        plot_type=plot_type,
        start_time=start_time,
        forecast_time=forecast_time,
        verbose=verbose
    )


def show_plot(
        plot_type: str,
        start_time: str or datetime.datetime or pd.Timestamp,
        forecast_time: str or pd.Timedelta,
        presenter: Presenter = IPythonPresenter(),
        verbose: Union[bool, int] = False
):
    """Draw images and show them in Jupyter Notebook.

    Parameters
    ----------
    plot_type : str
        Plot type according to systems.
    start_time: str or datetime.datetime or pd.Timestamp
        Start time:`
            - str: YYYYMMDDHH
            - datetime.datetime or pd.Timestamp
    forecast_time: str or pd.Timedelta
        Forecast time duration, such as 3h.
    presenter: Presenter
        image presenter
    verbose

    Raises
    -------
    ValueError
        plot_type is not found
    """
    system = SYSTEM_NAME
    from sokort.interface import show_plot as base_show_plot
    return base_show_plot(
        system=system,
        plot_type=plot_type,
        start_time=start_time,
        forecast_time=forecast_time,
        presenter=presenter,
        verbose=verbose
    )


def get_plotter_class(plot_type: str) -> Optional[Type[SystemNclPlotter]]:
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
