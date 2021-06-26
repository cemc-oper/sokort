import click

from sokort.config import load_config
from sokort.interface import draw_plot, show_plot
from sokort._presenter import PILPresenter
from sokort._util import fix_system_name


@click.group("sokort")
def cli():
    pass


@cli.command("draw")
@click.option("--config", "config_file_path", default=None, help="config file path")
@click.option("--system", "system_name", required=True, help="operation system name")
@click.option("--plot-type", required=True, help="plot type")
@click.option("--start-time", required=True, help="start time, YYYYMMDDHH")
@click.option("--forecast-time", required=True, help="forecast time in string format, 24h")
@click.option("--data-dir", default=None, help="data directory.")
@click.option("--work-dir", default=None, help="work directory.")
def draw(
        config_file_path: str,
        system_name: str,
        plot_type: str,
        start_time: str,
        forecast_time: str,
        data_dir,
        work_dir
):
    system_name = fix_system_name(system_name)
    if config_file_path is not None:
        load_config(config_file_path)

    draw_plot(
        system=system_name,
        plot_type=plot_type,
        start_time=start_time,
        forecast_time=forecast_time,
        data_directory=data_dir,
        work_directory=work_dir,
        verbose=2
    )


@cli.command("show")
@click.option("--config", "config_file_path", default=None, help="config file path")
@click.option("--system", "system_name", required=True, help="operation system name")
@click.option("--plot-type", required=True, help="plot type")
@click.option("--start-time", required=True, help="start date, YYYYMMDDHH")
@click.option("--forecast-time", required=True, help="forecast time, 24h")
def show(
        config_file_path: str,
        system_name: str,
        plot_type: str,
        start_time: str,
        forecast_time: str
):
    system_name = fix_system_name(system_name)
    if config_file_path is not None:
        load_config(config_file_path)

    show_plot(
        system=system_name,
        plot_type=plot_type,
        start_time=start_time,
        forecast_time=forecast_time,
        presenter=PILPresenter(),
        verbose=2,
    )


if __name__ == "__main__":
    cli()
