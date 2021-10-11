import datetime
import os
from pathlib import Path
from typing import Dict, Optional, Union
import shutil

import pandas as pd

from sokort._logging import get_logger
from sokort._util import (
    get_work_dir,
    get_data_path
)
from sokort.config import Config
from sokort.systems.grapes_gfs_gmf._plotter import SystemNclPlotter
from sokort._plotter import PythonPlotter

logger = get_logger("grapes_gfs_gmf")


class TyphoonPlotter(SystemNclPlotter):
    """
    Plotter for component typhoon.
    """
    def __init__(self, task: Dict, work_dir: str, config: Dict, **kwargs):
        SystemNclPlotter.__init__(self, task, work_dir, config, **kwargs)
        self.typhoon_area = task["typhoon_area"]

    @classmethod
    def create_plotter(
            cls,
            graphics_config: Config,
            start_time: Union[datetime.datetime, pd.Timestamp],
            forecast_time: pd.Timedelta = None,
            data_directory: Optional[Union[str, Path]] = None,
            work_directory: Optional[Union[str, Path]] = None,
            verbose: Union[bool, int] = False,
            **kwargs
    ):
        """Create plotter

        Parameters
        ----------
        graphics_config: dict
            graphics config
        start_time: datetime.datetime or pd.Timestamp
            Start hour
        forecast_time: pd.Timedelta
            Forecast time duration, such as 3h.
        data_directory:
        work_directory:
        verbose:

        Returns
        -------
        SystemNclPlotter
        """
        data_path = get_data_path(
            system_name=cls.system_name,
            start_time=start_time,
            forecast_time=forecast_time,
            data_directory=data_directory
        )
        if verbose:
            logger.debug(f"data directory: {data_path}")

        system_config = graphics_config["systems"]["grapes_gfs_gmf"]
        component_config = system_config["components"]["typhoon"]

        task = {
            "ncl_dir": os.path.expandvars(component_config["ncl_dir"]),
            "script_dir": os.path.expandvars(system_config["system"]["script_dir"]),
            "data_path": data_path,
            "start_datetime": start_time.isoformat(),
            "forecast_time": forecast_time,
            "typhoon_area": kwargs["typhoon_area"]
        }

        # work dir
        work_dir = get_work_dir(
            graphics_config=graphics_config,
            work_directory=work_directory
        )
        if verbose:
            logger.debug(f"work directory: {work_dir.absolute()}")

        config = {
            "ncl_lib": os.path.expandvars(graphics_config["ncl"]["ncl_lib"]),
            "geodiag_root": os.path.expandvars(graphics_config["ncl"]["geodiag_root"]),
            "load_env_script": graphics_config["ncl"]["load_env_script"],
        }

        return cls(
            task=task,
            work_dir=work_dir,
            config=config,
            verbose=verbose
        )


class TyphoonPythonPlotter(PythonPlotter):
    plot_types = None
    system_name = "grapes_gfs_gmf"

    def __init__(
            self,
            task: Dict,
            work_dir: Union[str, Path],
            config: Dict,
            verbose: Union[bool, int] = False,
            **kwargs
    ):
        """
        Parameters
        ----------
        task
            task config dict
            {
                "script_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script",
                "data_path": "/sstorage1/COMMONDATA/OPER/NWPC/GRAPES_GFS_GMF/Prod-grib/2020011021/ORIG/",
                "start_datetime": "2021-06-23 00:00:00",
                "forecast_time": "3h",
            }
        work_dir
            work directory
        config
            service config
            {
            }
        """
        super(TyphoonPythonPlotter, self).__init__(
            task=task,
            work_dir=work_dir,
            config=config,
            verbose=verbose,
            **kwargs
        )
        self.run_script_name = "run_python.sh"
        self.python_script_name = None

    def _check_validity(self):
        if self.python_script_name is None:
            raise ValueError("python_script_name should be set.")

    @classmethod
    def create_plotter(
            cls,
            graphics_config: Config,
            start_time: Union[datetime.datetime, pd.Timestamp],
            forecast_time: pd.Timedelta = None,
            data_directory: Optional[Union[str, Path]] = None,
            work_directory: Optional[Union[str, Path]] = None,
            verbose: Union[bool, int] = False,
            **kwargs
    ):
        """Create plotter

        Parameters
        ----------
        graphics_config
            graphics config
        start_time
        forecast_time
            Forecast time duration, such as 3h.
        data_directory
            data directory for whole cycle.
        work_directory
            work directory to run plot script.
        verbose
            logger setting

        Returns
        -------
        SystemNclPlotter
        """
        system_config = graphics_config["systems"][cls.system_name]

        data_path = get_data_path(
            system_name=cls.system_name,
            start_time=start_time,
            forecast_time=forecast_time,
            data_directory=data_directory
        )
        if verbose:
            logger.debug(f"data directory: {data_path}")

        # task
        component_config = system_config["components"]["typhoon"]

        task = {
            "script_dir": os.path.expandvars(component_config["python_script_dir"]),
            "data_path": data_path,
            "start_datetime": start_time.isoformat(),
            "forecast_time": forecast_time,
            **kwargs
        }

        # work dir
        work_dir = get_work_dir(
            graphics_config=graphics_config,
            work_directory=work_directory
        )
        if verbose:
            logger.debug(f"work directory: {work_dir.absolute()}")

        # config settings
        config = {
            "load_env_script": graphics_config["python"]["load_env_script"],
        }

        return cls(
            task=task,
            work_dir=work_dir,
            config=config,
            verbose=verbose,
            **kwargs
        )

    def _prepare_environment(self):
        python_script_name = self.python_script_name  # "ENPO_plot_tbb.py"

        script_dir = self.task["script_dir"]
        # str "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script"

        # create environment
        Path(self.work_dir).mkdir(parents=True, exist_ok=True)
        os.chdir(self.work_dir)

        try:
            shutil.copy2(f"{script_dir}/{python_script_name}", f"{python_script_name}")
        except shutil.SameFileError:
            pass

        try:
            shutil.copy2(f"{str(self.run_script_path)}", self.run_script_path.name)
        except shutil.SameFileError:
            pass

        try:
            shutil.copy2(f"{str(self.load_env_script_path)}", self.load_env_script_path.name)
        except shutil.SameFileError:
            pass

    def _generate_environ(self):
        python_script_name = self.python_script_name

        data_path = self.task["data_path"]
        # str "/sstorage1/COMMONDATA/OPER/NWPC/GRAPES_GFS_GMF/Prod-grib/2020011021/ORIG/"

        envs = os.environ
        envs.update({
            "start_time": self.start_time,
            "forecast_hour": self.forecast_hour,
            "data_path": data_path,
            "python_script_name": python_script_name,
        })
        return envs

    @classmethod
    def _get_run_script(cls):
        return Path(Path(__file__).parent, "run_python.sh")
