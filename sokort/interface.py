import datetime
from typing import Union

import pandas as pd

from ._logging import get_logger, convert_verbose
from .config import get_config
from ._util import fix_system_name, parse_start_time, parse_forecast_time
from ._presenter import Presenter, IPythonPresenter


logger = get_logger()


def get_plotter_class(system, plot_type):
    if system == "grapes_gfs_gmf":
        from sokort.systems.grapes_gfs_gmf import get_plotter_class as get_plotter_class_for_system
        return get_plotter_class_for_system(plot_type)
    elif system == "grapes_meso_3km":
        from sokort.systems.grapes_meso_3km import get_plotter_class as get_plotter_class_for_system
        return get_plotter_class_for_system(plot_type)
    else:
        raise ValueError(f"system is not supported: {system}")


def draw_plot(
        system: str,
        plot_type: str,
        start_time: Union[str, datetime.datetime, pd.Timestamp],
        forecast_time: Union[str, pd.Timedelta] = None,
        data_directory = None,
        work_directory = None,
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
        verbose: Union[bool, int] = False
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
        verbose=verbose
    )

    plotter.run_plot()

    presenter.show_plot(plotter.get_image_list())

    return
