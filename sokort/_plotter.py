import os
import subprocess
from typing import Union, Dict, List
from pathlib import Path

import pandas as pd

from ._logging import get_logger, convert_verbose
from ._util import get_forecast_hour


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
                    "start_datetime": "2020-11-12 00:00:00", # time string supported by ``pd.to_datetime``
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
        verbose: bool or int
            print setting

                - `0`: hide all prints
                - `1`: only print logger outputs
                - `2`: print both logger and script outputs
        """
        self.task = task
        self.work_dir = work_dir
        self.config = config
        self.ncl_script_name = None

        self.verbose = convert_verbose(verbose)

        # magic options
        self.run_script_name = "run_ncl.sh"
        if (
                "load_env_script" not in config
                or (isinstance(config["load_env_script"], str) and len(config["load_env_script"]) == 0)
        ):
            load_env_script = _get_load_env_script()
        else:
            load_env_script = Path(config["load_env_script"])

        self.load_env_script_path = load_env_script
        self.run_script_path = self._get_run_script()

        # time options for task.
        self.start_datetime = pd.to_datetime(self.task["start_datetime"])
        self.start_time = self.start_datetime.strftime("%Y%m%d%H")  # 2020011100

        if "forecast_time" in self.task and self.task["forecast_time"] is not None:
            self.forecast_timedelta = pd.Timedelta(self.task["forecast_time"])
            self.forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"  # 003
            self.forecast_datetime = self.start_datetime + self.forecast_timedelta
            self.forecast_time = self.forecast_datetime.strftime("%Y%m%d%H")  # 2020011103
        else:
            self.forecast_timedelta = None
            self.forecast_hour = None
            self.forecast_datetime = self.start_datetime
            self.forecast_time = self.forecast_datetime.strftime("%Y%m%d%H")  # 2020011103

    def run_plot(self):
        """
        Run process to draw plot in work_dir.
        """
        self._check_validity()
        self._prepare_environment()
        envs = self._generate_environ()
        self._run_process(envs=envs)
        self._do_postprocess()

    def _check_validity(self):
        if self.ncl_script_name is None:
            raise ValueError("ncl_script_name should be set.")

    def _prepare_environment(self):
        """
        Prepare working directory environment. Such as:

            * copy scripts
            * link resources
            * create config files
        """
        pass

    def _generate_environ(self):
        """
        Generate environment variables for running plotting script.
        """
        envs = os.environ
        return envs

    def _run_process(self, envs: Dict):
        """
        Run plotting script (usually it is a shell script) under environment variables ``envs``.
        """
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

    def _do_postprocess(self):
        image_list = self.get_image_list()
        for item in image_list:
            image_path = Path(item["path"])
            image_name = image_path.stem
            ps_image_path = f"{image_name}.ps"
            self.convert_image(ps_image_path)

    def get_image_list(self) -> List:
        """
        Get image list.

        Should implemented by sub-class.

        Returns
        -------
        image_list: list
            Image list.
        """
        raise NotImplemented()

    def convert_image(self, file_path):
        if self.verbose >= 1:
            logger.debug(f"convert image: {file_path}")

        process_stdout = subprocess.DEVNULL
        process_stderr = subprocess.DEVNULL
        if self.verbose >= 2:
            process_stdout = None
            process_stderr = None

        pipe = subprocess.Popen(
            ["ksh",  _get_convert_image_script(), file_path],
            start_new_session=True,
            stdout=process_stdout,
            stderr=process_stderr
        )

        stdout, stderr = pipe.communicate()
        pipe.wait()
        pipe.terminate()
        if self.verbose >= 1:
            logger.debug(f"convert image done: {file_path}")

    @classmethod
    def _get_run_script(cls):
        return None


def _get_load_env_script():
    return Path(Path(__file__).parent, "load_env.sh")


def _get_convert_image_script():
    return Path(Path(__file__).parent, "convert_image.sh")
