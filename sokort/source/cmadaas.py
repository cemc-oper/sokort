from typing import List
from pathlib import Path


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
}


def generate_filenames(file_path: Path) -> List[str]:
    """
    根据 CMADaaS 格式文件名生成 CEMC 格式文件名

    Z_NAFP_C_BABJ_20220722000000_P_NWPC-GRAPES-GFS-GLB-19800.grib2

    Parameters
    ----------
    file_path
        CMADaaS格式文件名

    Returns
    -------
    List[str]
        绘图脚本支持的文件名列表
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
