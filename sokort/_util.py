import pandas as pd


def get_forecast_hour(forecast_time: pd) -> int:
    return int(forecast_time.total_seconds()) // 3600
