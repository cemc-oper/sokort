import datetime
import tempfile
from pathlib import Path

from nwpc_graphics.systems.grapes_gfs_gmf._plotter import SystemPlotter


class GamsPlotter(SystemPlotter):
    """
    Plotter for component GAMS.
    """
    def __init__(self, task: dict, work_dir: str, config: dict):
        SystemPlotter.__init__(self, task, work_dir, config)

    @classmethod
    def create_plotter(
            cls,
            graphics_config: dict,
            start_date: str,
            start_time: str,
            forecast_time: str):
        """Create plotter

        Parameters
        ----------
        graphics_config: dict
            graphics config
        start_date: str
            Start date, YYYYMMDD
        start_time: str
            Start hour, HH
        forecast_time: str
            Forecast time duration, such as 3h.

        Returns
        -------
        SystemPlotter
        """
        start_datetime = datetime.datetime.strptime(f"{start_date}{start_time}", "%Y%m%d%H")
        start_datetime_4dvar = start_datetime - datetime.timedelta(hours=3)
        start_time_4dvar = start_datetime_4dvar.strftime("%Y%m%d%H")

        system_config = graphics_config["systems"]["grapes_gfs_gmf"]
        component_config = system_config["components"]["gams"]

        task = {
            "ncl_dir": component_config["ncl_dir"],
            "script_dir": system_config["system"]["script_dir"],
            "data_path": system_config["data"]["data_path"].format(
                start_time_4dvar=start_time_4dvar
            ),
            "start_datetime": start_datetime.isoformat(),
            "forecast_time": forecast_time,
        }

        work_dir = tempfile.mkdtemp()

        config = {
            "ncl_lib": graphics_config["ncl"]["ncl_lib"],
            "geodiag_root": graphics_config["ncl"]["geodiag_root"],
        }

        return cls(
            task=task,
            work_dir=work_dir,
            config=config,
        )

    @classmethod
    def _get_run_script(cls):
        return Path(Path(__file__).parent, "run_ncl.sh")
