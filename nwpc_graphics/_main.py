import importlib

import click

from nwpc_graphics import load_config
from nwpc_graphics._presenter import PILPresenter


@click.group("nwpc_graphics")
def cli():
    pass


@cli.command("draw")
@click.option("--config", "config_file_path", default=None, help="config file path")
@click.option("--system", "system_name", required=True, help="operation system name")
@click.option("--plot-type", required=True, help="plot type")
@click.option("--start-date", required=True, help="start date, YYYYMMDD")
@click.option("--start-time", required=True, help="start hour, HH")
@click.option("--forecast-time", required=True, help="forecast time, 24h")
def draw(
        config_file_path: str,
        system_name: str,
        plot_type: str,
        start_date: str,
        start_time: str,
        forecast_time: str
):
    if config_file_path is not None:
        load_config(config_file_path)

    module = importlib.import_module(f"nwpc_graphics.systems.{system_name}")
    draw_plot = module.draw_plot
    draw_plot(
        plot_type=plot_type,
        start_date=start_date,
        start_time=start_time,
        forecast_time=forecast_time,
    )


@cli.command("show")
@click.option("--config", "config_file_path", default=None, help="config file path")
@click.option("--system", "system_name", required=True, help="operation system name")
@click.option("--plot-type", required=True, help="plot type")
@click.option("--start-date", required=True, help="start date, YYYYMMDD")
@click.option("--start-time", required=True, help="start hour, HH")
@click.option("--forecast-time", required=True, help="forecast time, 24h")
def show(
        config_file_path: str,
        system_name: str,
        plot_type: str,
        start_date: str,
        start_time: str,
        forecast_time: str
):
    if config_file_path is not None:
        load_config(config_file_path)

    module = importlib.import_module(f"nwpc_graphics.systems.{system_name}")
    show_plot = module.show_plot
    show_plot(
        plot_type=plot_type,
        start_date=start_date,
        start_time=start_time,
        forecast_time=forecast_time,
        presenter=PILPresenter(),
    )


if __name__ == "__main__":
    cli()
