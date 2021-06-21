import datetime
import os
import subprocess
from typing import Union, Dict, List
from pathlib import Path

import pandas as pd

from ._logging import get_logger


logger = get_logger()


class BasePlotter(object):
    """
    Base class for plotter using NCL.
    """
    plot_types = None

    def __init__(
            self,
            task: Dict,
            work_dir: Union[str, Path],
            config: Dict,
            verbose: Union[bool, int] = False
    ):
        """
        Parameters
        ----------
        task: dict
            task config dict

                {
                    "start_datetime": datetime.datetime(2020, 1, 11, 0).isoformat(),
                    "forecast_time": "3h", # optional
                }
        work_dir: str
            work directory
        config: dict
            service config
                {
                    "ncl_lib": "/home/wangdp/project/graph/ncllib",
                    "geodiag_root": "/home/wangdp/project/graph/GEODIAG",
                    "load_env_script": "",
                }
        verbose:
            print setting

                - `0`: hide all prints
                - `1`: only print logger outputs
                - `2`: print logger and script outputs
        """
        self.task = task
        self.work_dir = work_dir
        self.config = config
        self.ncl_script_name = None

        self.verbose = verbose
        if isinstance(self.verbose, bool):
            if self.verbose:
                self.verbose = 1
            else:
                self.verbose = 0

        # magic options
        self.run_script_name = "run_ncl.sh"
        if (
                "load_env_script" not in config
                or (isinstance(config["load_env_script"], str) and len(config["load_env_script"]) == 0)
        ):
            load_env_script = _get_load_env_script()
        else:
            load_env_script = config["load_env_script"]

        self.load_env_script_path = load_env_script
        self.run_script_path = self._get_run_script()

        # time options for task.
        self.start_datetime = datetime.datetime.fromisoformat(self.task["start_datetime"])
        self.start_time = self.start_datetime.strftime("%Y%m%d%H")  # 2020011100

        if "forecast_time" in self.task:
            self.forecast_timedelta = pd.Timedelta(self.task["forecast_time"]).to_pytimedelta()
            self.forecast_datetime = self.start_datetime + self.forecast_timedelta
            self.forecast_hour = f"{int(self.forecast_timedelta.total_seconds()) // 3600:03}"  # 003
            self.forecast_time = self.forecast_datetime.strftime("%Y%m%d%H")  # 2020011103

    def run_plot(self):
        """
        Run process to draw plot in work_dir.
        """
        self._check_validity()
        self._prepare_environment()
        envs = self._generate_environ()
        self._run_process(envs=envs)

    def _check_validity(self):
        if self.ncl_script_name is None:
            raise ValueError("ncl_script_name should be set.")

    def _prepare_environment(self):
        pass

    def _generate_environ(self):
        envs = os.environ
        return envs

    def _run_process(self, envs: dict):
        if self.verbose >= 1:
            logger.debug(f"run process: {self.run_script_name}")
        process_stdout = subprocess.DEVNULL
        process_stderr = subprocess.DEVNULL
        if self.verbose >= 2:
            process_stdout = None
            process_stderr = None
        pipe = subprocess.Popen(
            ["bash",  f"./{self.run_script_name}"],
            start_new_session=True,
            env=envs,
            stdout=process_stdout,
            stderr=process_stderr
        )

        stdout, stderr = pipe.communicate()
        pipe.wait()
        pipe.terminate()
        if self.verbose >= 1:
            logger.debug(f"run process done: {self.run_script_name}")

    def get_image_list(self) -> List:
        """Get image list.

        Should implemented by sub-class.

        Returns
        -------
        image_list: list
            Images list.
        """
        raise NotImplemented()

    @classmethod
    def _get_run_script(cls):
        return None


def _get_load_env_script():
    return Path(Path(__file__).parent, "load_env.sh")
