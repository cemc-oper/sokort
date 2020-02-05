from pathlib import Path
import datetime
import os
import shutil
import subprocess

import pytimeparse

from nwpc_graphics._util import _get_load_env_script


class BasePlotter(object):
    """
    Base class for plotter.
    """
    plot_types = None

    def __init__(self, task: dict, work_dir: str, config: dict):
        """
        Parameters
        ----------
        task: dict
            task config dict
            {
                "script_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script",
                "data_path": "/sstorage1/COMMONDATA/OPER/NWPC/GRAPES_GFS_GMF/Prod-grib/2020011021/ORIG/",
                "start_datetime": datetime.datetime(2020, 1, 11, 0).isoformat(),
                "forecast_time": "3h",
            }
        work_dir: str
            work directory
        config: dict
            service config
            {
                "ncl_lib": "/home/wangdp/project/graph/ncllib",
                "geodiag_root": "/home/wangdp/project/graph/GEODIAG",
            }
        """
        self.task = task
        self.work_dir = work_dir
        self.config = config
        self.ncl_script_name = None

        # magic options
        self.run_script_name = "run_ncl.sh"
        self.load_env_script_path = _get_load_env_script()

        # time options for task.

        self.start_datetime = datetime.datetime.fromisoformat(self.task["start_datetime"])
        # datetime.datetime, such as datetime.datetime(2020, 1, 11, 0)

        self.forecast_timedelta = datetime.timedelta(seconds=pytimeparse.parse(self.task["forecast_time"]))
        # datetime.timedelta, such as datetime.timedelta(hours=3)

        self.forecast_datetime = self.start_datetime + self.forecast_timedelta

        self.start_time = self.start_datetime.strftime("%Y%m%d%H")  # 2020011100
        self.forecast_hour = f"{int(self.forecast_timedelta.total_seconds()) // 3600:03}"  # 003
        self.forecast_time = self.forecast_datetime.strftime("%Y%m%d%H")  # 2020011103

    def run_plot(self):
        """
        Run ncl script to draw plot in work_dir.
        """
        if self.ncl_script_name is None:
            raise ValueError("ncl_script_name should be set.")
        self._prepare_environment()
        envs = self._generate_environ()
        self._run_process(envs)

    def show_plot(self):
        """Show images in IPython.
        """
        image_list = self._get_image_list()
        from IPython.display import Image, display
        for an_image in image_list:
            display(Image(filename=f"./{an_image['path']}"))

    def _prepare_environment(self):
        ncl_script_name = self.ncl_script_name  # "GFS_GRAPES_PWAT_SFC_AN_AEA.ncl"

        script_dir = self.task["script_dir"]
        # str /home/wangdp/project/graph/operation/NWP_GRAPES_MESO_3KM_POST/tograph/script/

        # create environment
        Path(self.work_dir).mkdir(parents=True, exist_ok=True)
        os.chdir(self.work_dir)

        with open("grapes_meso_date", "w") as f:
            f.write(f"{self.start_time}{self.forecast_hour}\n")
            f.write(f"{self.forecast_time}")

        shutil.copy2(f"{script_dir}/ps2gif_NoRotation_NoPlot.scr", "ps2gif_NoRotation_NoPlot.src")
        shutil.copy2(f"{script_dir}/{ncl_script_name}", f"{ncl_script_name}")

        component_directory = Path(__file__).parent
        run_ncl_script_path = Path(component_directory, self.run_script_name)
        shutil.copy2(f"{str(run_ncl_script_path)}", self.run_script_name)
        shutil.copy2(f"{str(self.load_env_script_path)}", self.load_env_script_path.name)

    def _generate_environ(self):
        ncl_script_name = self.ncl_script_name

        script_dir = self.task["script_dir"]

        geodiag_root = self.config["geodiag_root"]  # "/home/wangdp/project/graph/GEODIAG"
        geodiag_tools = str(Path(geodiag_root, "tools"))

        data_path = self.task["data_path"]
        # str "/sstorage1/COMMONDATA/OPER/NWPC/GRAPES_GFS_GMF/Prod-grib/2020011021/ORIG/"

        envs = os.environ
        envs.update({
            "GEODIAG_ROOT": geodiag_root,
            "GEODIAG_TOOLS": geodiag_tools,
            "start_time": self.start_time,
            "data_path": data_path,
            "script_dir": script_dir,
            "ncl_script_name": ncl_script_name,
        })
        return envs

    def _run_process(self, envs: dict):
        pipe = subprocess.Popen(
            [f"./{self.run_script_name}"],
            start_new_session=True,
            env=envs
        )

        stdout, stderr = pipe.communicate()
        pipe.wait()
        pipe.terminate()

    def _get_image_list(self):
        """Get image list.

        Should implemented by sub-class.

        Returns
        -------
        image_list: list
            Images list.
        """
        raise NotImplemented()
