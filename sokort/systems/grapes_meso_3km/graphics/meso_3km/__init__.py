from pathlib import Path
import os
import shutil
import datetime

import pandas as pd

from nwpc_data.data_finder import find_local_file

from sokort.systems.grapes_meso_3km._plotter import SystemPlotter
from sokort._config import Config


class Meso3kmPlotter(SystemPlotter):
    """
    """
    plot_types = None

    def __init__(
            self,
            task: dict,
            work_dir: str,
            config: dict,
    ):
        SystemPlotter.__init__(
            self,
            task=task,
            work_dir=work_dir,
            config=config,
        )

    @classmethod
    def create_plotter(
            cls,
            graphics_config: Config,
            start_time: datetime.datetime or pd.Timestamp,
            forecast_time: pd.Timedelta):
        """Create plotter

        Parameters
        ----------
        graphics_config: Config
            graphics config
        start_time: datetime.datetime or pd.Timestamp
        forecast_time: pd.Timedelta
            Forecast time duration, such as 3h.

        Returns
        -------
        SystemPlotter
        """
        data_file = find_local_file(
            "grapes_meso_3km/grib2/orig",
            start_time=start_time,
            forecast_time=forecast_time,
        )
        data_path = str(data_file.parent) + "/"

        system_config = graphics_config["systems"]["grapes_meso_3km"]
        component_config = system_config["components"]["meso_3km"]
        task = {
            "script_dir": component_config["system"]["script_dir"],
            "data_path": data_path,
            "start_datetime": start_time.isoformat(),
            "forecast_time": forecast_time,
        }
        work_dir = graphics_config.generate_run_dir()
        config = {
            "ncl_lib": graphics_config["ncl"]["ncl_lib"],
            "geodiag_root": graphics_config["ncl"]["geodiag_root"],
            "load_env_script": graphics_config["ncl"]["load_env_script"],
        }

        return cls(
            task=task,
            work_dir=work_dir,
            config=config
        )
