from pathlib import Path
import shutil

import pandas as pd

from sokort._logging import get_logger
from sokort.systems.grapes_gfs_gmf._plotter import SystemNclPlotter


logger = get_logger("grapes_gfs_gmf")


class T2MExtremsPlotter(SystemNclPlotter):
    """
    Plotter for component Extrems.
    """
    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemNclPlotter.__init__(self, task, work_dir, config, **kwargs)
        self.forecast_hour = "T2MExt"
        self.min_forecast_time = self.forecast_hour
        self.max_forecast_time = self.forecast_hour

    def _prepare_environment(self):
        SystemNclPlotter._prepare_environment(self)

        # NOTE: grapes_meso_data is needed by T2MMAX/T2MMIN plots.
        forecast_datetime = self.start_datetime + pd.to_timedelta("24h")
        with open("grapes_meso_date", "w") as f:
            f.write(f"{self.start_time}024\n")
            f.write(f"{forecast_datetime.strftime('%Y%m%d%H')}")

    @classmethod
    def _get_run_script(cls):
        return Path(Path(__file__).parent, "run_ncl.sh")
