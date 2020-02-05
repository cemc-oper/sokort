import pathlib

from nwpc_graphics._util import load_plotters_from_paths

if __name__ == "__main__":
    plotters = load_plotters_from_paths([pathlib.Path(pathlib.Path(__file__).parent, "graphics")])
    print(plotters)
