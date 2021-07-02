from typing import Union, Optional
from pathlib import Path
import datetime

import pandas as pd

from ._data_finder import find_local_file
from .config import Config


def get_forecast_hour(forecast_time: pd) -> int:
    return int(forecast_time.total_seconds()) // 3600


def get_data_path(
        system_name: str,
        start_time: Union[datetime.datetime, pd.Timestamp],
        forecast_time: pd.Timedelta = None,
        data_directory: Optional[Union[str, Path]] = None,
):
    if data_directory is None:
        # get data file using nwpc-data.
        if forecast_time is None:
            forecast_time = pd.to_timedelta("0h")
        data_file = find_local_file(
            f"{system_name}/grib2/orig",
            start_time=start_time,
            forecast_time=forecast_time,
        )
        if data_file is None:
            raise FileNotFoundError(f"data file not found: {system_name}, {start_time}, {forecast_time}")
        data_path = str(data_file.parent) + "/"
    else:
        data_path = data_directory
        if data_path[-1] != "/":
            data_path = data_path + "/"
    return data_path


def get_work_dir(
        graphics_config: Config,
        system_name: str = None,
        start_time: Union[datetime.datetime, pd.Timestamp] = None,
        forecast_time: pd.Timedelta = None,
        work_directory: Optional[Union[str, Path]] = None,
):
    if work_directory is None:
        work_dir = graphics_config.generate_run_dir()
    else:
        work_dir = Path(work_directory)
    return work_dir


def fix_system_name(system):
    system_mapper = {
        "grapes_gfs": "grapes_gfs_gmf"
    }
    return system_mapper.get(system, system)


def parse_start_time(start_time: Union[str, datetime.datetime, pd.Timestamp]):
    if isinstance(start_time, str):
        if len(start_time) == 10:
            start_time = pd.to_datetime(start_time, format="%Y%m%d%H")
        else:
            start_time = pd.to_datetime(start_time)
    return start_time


def parse_forecast_time(forecast_time: Union[str, pd.Timedelta]):
    if isinstance(forecast_time, str):
        forecast_time = pd.to_timedelta(forecast_time)
    return forecast_time
