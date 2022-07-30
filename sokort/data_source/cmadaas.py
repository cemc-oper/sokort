from datetime import datetime
from typing import List, Union, Optional
from pathlib import Path

import yaml
import pandas as pd
from jinja2 import Template


production_mapper = {
    "GRAPES-GFS-GLB": {
        "filename_template": "gmf.gra.{start_time_string}{forecast_hour_string}.grb2",
        "stream": "oper",
    },
    "GRAPES-3KM-ORIG": {
        "filename_template": [
            "rmf.hgra.{start_time_string}{forecast_hour_string}.grb2",
            "rmf.gra.{start_time_string}{forecast_hour_string}.grb2",
        ],
        "stream": "oper",
    },
    "GRAPES-TYM-ACWP": {
        "filename_template": "rmf.gra.{start_time_string}{forecast_hour_string}.grb2",
        "stream": "oper",
    },
    "GRAPES-GEPS-GLB": {
        "filename_template": "gef.gra.{number_string}.{start_time_string}{forecast_hour_string}.grb2",
        "stream": "ens",
    },
    "GRAPES-REPS-CN": {
        "filename_template": "mef.gra.{number_string}.{start_time_string}{forecast_hour_string}.grb2",
        "stream": "ens",
    },
}


class Config:
    def __init__(self):
        self.systems = dict()
        self.labels = dict()

    @classmethod
    def load_config(cls, config_file=None) -> "Config":
        if config_file is None:
            config_file = Path(Path(__file__).parent, "cmadaas.yaml")
        with open(config_file) as f:
            config_dict = yaml.safe_load(f)
        c = Config()
        for system_name, system_config in config_dict.items():
            c.systems[system_name] = system_config
            c.labels[system_config["production_label"]] = system_name
        return c


def load_config() -> Config:
    global cmadaas_config
    cmadaas_config = Config.load_config()
    return cmadaas_config


cmadaas_config: Config = load_config()


def get_config() -> Config:
    if cmadaas_config is None:
        raise ValueError("CMADaaS config must be set.")
    else:
        return cmadaas_config


def get_file_directory(
        system: str,
        start_time: Union[datetime, pd.Timestamp],
        forecast_time: Optional[pd.Timedelta],
) -> str:
    config = get_config()
    system_config = config.systems[system]
    template_string = system_config["location"]

    time_vars = TimeVars(start_time=start_time, forecast_time=forecast_time)

    template = Template(template_string)
    location = template.render(time_vars=time_vars)
    return location


def get_file_name(
        system: str,
        start_time: Union[datetime, pd.Timestamp],
        forecast_time: Union[pd.Timedelta, str],
        **kwargs
) -> str:
    config = get_config()
    system_config = config.systems[system]
    template_string = system_config["file_name"]

    time_vars = TimeVars(start_time=start_time, forecast_time=forecast_time)
    query_vars = QueryVars()
    for key in kwargs:
        setattr(query_vars, key, kwargs[key])

    template = Template(template_string)
    file_name = template.render(time_vars=time_vars, query_vars=query_vars)
    return file_name


def generate_filenames(file_path: Path) -> List[str]:
    """
    根据 CMADaaS 格式文件名生成 CEMC 格式文件名列表。

    CMADaaS 格式文件名类似：

    - CMA-GFS: Z_NAFP_C_BABJ_20220722000000_P_NWPC-GRAPES-GFS-GLB-19800.grib2
    - CMA-MESO: Z_NAFP_C_BABJ_20220701210000_P_NWPC-GRAPES-3KM-ORIG-02400.grb2
    - CMA-TYM: Z_NAFP_C_BABJ_20220701180000_P_NWPC-GRAPES-TYM-ACWP-02400.grib2
    - CMA-GEPS: Z_NAFP_C_BABJ_20220701120000_P_NWPC-GRAPES-GEPS-GLB-26400-m012.grib2
    - CMA-REPS: Z_NAFP_C_BABJ_20220701120000_P_NWPC-GRAPES-REPS-CN-08200-m012.grib2

    Parameters
    ----------
    file_path
        CMADaaS格式文件名

    Returns
    -------
    List[str]
        绘图脚本支持的文件名列表

    Examples
    ---------
    1. CMA-GFS

        >>> generate_filenames(Path("Z_NAFP_C_BABJ_20220722000000_P_NWPC-GRAPES-GFS-GLB-19800.grib2"))
        ['gmf.gra.2022072200198.grb2']

    2. CMA-MESO

        >>> generate_filenames(Path("Z_NAFP_C_BABJ_20220701210000_P_NWPC-GRAPES-3KM-ORIG-02400.grb2"))
        ['rmf.hgra.2022070121024.grb2', 'rmf.gra.2022070121024.grb2']

    3. CMA-TYM

        >>> generate_filenames(Path("Z_NAFP_C_BABJ_20220701180000_P_NWPC-GRAPES-TYM-ACWP-02400.grib2"))
        ['rmf.gra.2022070118024.grb2']

    4. CMA-GEPS

        >>> generate_filenames(Path("Z_NAFP_C_BABJ_20220701120000_P_NWPC-GRAPES-GEPS-GLB-26400-m012.grib2"))
        ['gef.gra.012.2022070112264.grb2']

    5. CMA-REPS

        >>> generate_filenames(Path("Z_NAFP_C_BABJ_20220701120000_P_NWPC-GRAPES-REPS-CN-08200-m012.grib2"))
        ['mef.gra.012.2022070112082.grb2']

    """
    file_name_stem = file_path.stem
    start_time_string = file_name_stem[14:24]  # YYYYMMDDHH
    tokens = file_name_stem.split("-")

    forecast_hour_string = tokens[4][0:3]  # FFF

    production_string = "-".join(tokens[1:4])

    if len(tokens) == 5:
        number_string = None
    elif len(tokens) == 6:
        number_string = tokens[5][1:]
    else:
        raise RuntimeError(f"file name is not supported: {file_name_stem}")

    if production_string not in production_mapper:
        raise RuntimeError(f"production is not supported: {production_string}")

    file_template = production_mapper[production_string]["filename_template"]

    if isinstance(file_template, str):
        file_template = [file_template]

    file_names = []
    for t in file_template:
        file_name = t.format(
            start_time_string=start_time_string,
            forecast_hour_string=forecast_hour_string,
            number_string=number_string
        )
        file_names.append(file_name)

    return file_names


def get_hour(forecast_time: pd.Timedelta) -> int:
    return int(forecast_time.seconds/3600) + forecast_time.days * 24


class QueryVars:
    def __init__(self):
        self.storage_base = None
        self.number = None


class TimeVars:
    def __init__(
            self,
            start_time: Union[datetime, pd.Timestamp],
            forecast_time: Union[pd.Timedelta, str] = pd.Timedelta(hours=0)
    ):
        self.Year = start_time.strftime("%Y")
        self.Month = start_time.strftime("%m")
        self.Day = start_time.strftime("%d")
        self.Hour = start_time.strftime("%H")
        self.Minute = start_time.strftime("%M")

        if isinstance(forecast_time, pd.Timedelta):
            self.Forecast = f"{get_hour(forecast_time):03}"
        else:
            self.Forecast = forecast_time
