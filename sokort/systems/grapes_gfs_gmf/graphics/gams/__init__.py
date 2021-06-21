import datetime
import tempfile
from pathlib import Path

import pandas as pd

from nwpc_data.data_finder import find_local_file

from sokort.systems.grapes_gfs_gmf._plotter import SystemPlotter


class GamsPlotter(SystemPlotter):
    """
    Plotter for component GAMS.
    """
    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

    @classmethod
    def create_plotter(
            cls,
            graphics_config: dict,
            start_time: datetime.datetime or pd.Timestamp,
            forecast_time: pd.Timedelta):
        """Create plotter

        Parameters
        ----------
        graphics_config: dict
            graphics config
        start_time: datetime.datetime or pd.Timestamp
            Start hour
        forecast_time: pd.Timedelta
            Forecast time duration, such as 3h.

        Returns
        -------
        SystemPlotter
        """
        data_file = find_local_file(
            "grapes_gfs_gmf/grib2/orig",
            start_time=start_time,
            forecast_time=forecast_time,
        )
        data_path = str(data_file.parent) + "/"

        system_config = graphics_config["systems"]["grapes_gfs_gmf"]
        component_config = system_config["components"]["gams"]

        task = {
            "ncl_dir": component_config["ncl_dir"],
            "script_dir": system_config["system"]["script_dir"],
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
            config=config,
        )

    @classmethod
    def _get_run_script(cls):
        return Path(Path(__file__).parent, "run_ncl.sh")
