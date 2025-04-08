import datetime
import os
import shutil
from typing import Union, Optional
from pathlib import Path
import pandas as pd

from sokort.config import Config
from sokort._plotter import PythonPlotter
from sokort._logging import get_logger
from sokort.util import (
    get_work_dir,
    get_data_path
)


logger = get_logger(__name__)


class WmcGlobalPythonPlotter(PythonPlotter):
    plot_types = None

    def __init__(
            self,
            task: dict,
            work_dir: Union[str, Path],
            config: dict,
            system_name: str = "cma_gfs",
            verbose: Union[bool, int] = False,
            **kwargs
    ):
        """
        Parameters
        ----------
        task
            task config dict
            {
                "python_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/graph/python",
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
        super(WmcGlobalPythonPlotter, self).__init__(
            task=task,
            work_dir=work_dir,
            config=config,
            verbose=verbose,
            **kwargs
        )
        self.system_name = system_name

        self.run_script_name = "run_python.sh"
        self.python_script_name = "plot_GFS_wmc.py"
        self.plot_name = None

    def _check_validity(self):
        if self.python_script_name is None:
            raise ValueError("python_script_name should be set.")

    @classmethod
    def create_plotter(
            cls,
            system_name: str,
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
        system_name
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
        system_config = graphics_config["systems"][system_name]

        data_path = get_data_path(
            system_name=system_name,
            start_time=start_time,
            forecast_time=forecast_time,
            data_directory=data_directory
        )
        if verbose:
            logger.debug(f"data directory: {data_path}")

        # task
        component_config = system_config["components"]["wmc"]

        task = {
            "python_dir": os.path.expandvars(str(Path(component_config["python_dir"], "global"))),
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
            system_name=system_name,
            verbose=verbose,
            **kwargs
        )

    def _prepare_environment(self):
        python_script_name = self.python_script_name  # "ENPO_plot_tbb.py"

        python_dir = self.task["python_dir"]

        # create environment
        Path(self.work_dir).mkdir(parents=True, exist_ok=True)
        os.chdir(self.work_dir)

        try:
            shutil.copy2(f"{python_dir}/{python_script_name}", f"{python_script_name}")
            shutil.copy2(f"{python_dir}/globalvar_wmc.py", f"globalvar_wmc.py")
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

        envs = os.environ
        additional_envs = {
            "python_script_name": python_script_name,
            "start_time": self.start_time,
            "forecast_hour": self.forecast_hour,
            "data_path": data_path,
            "figure_path": str(self.work_dir),
            "plot_name": self.plot_name,
        }
        envs.update(additional_envs)

        logger.info("print environment variables...")
        for key, value in additional_envs.items():
            print(f"export {key}={value}")
        logger.info("print environment variables...done")

        return envs

    @classmethod
    def _get_run_script(cls):
        return Path(Path(__file__).parent, "run_python.sh")
