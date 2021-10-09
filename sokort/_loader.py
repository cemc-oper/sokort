import inspect
import pathlib
import importlib.util
import sys
from typing import List, Type, Dict, Union, Tuple

from ._plotter import BasePlotter


def _load_module(file_path: pathlib.Path):
    """
    Load module in file.
    """
    module_name = file_path.stem
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def load_plotters_from_paths(
        paths: List,
        plotter_class: Union[Type[BasePlotter], Tuple[Type[BasePlotter]]],
) -> Dict[str, Type[BasePlotter]]:
    """
    Load plotter classes from path list.

    Parameters
    ----------
    paths: List[Union[pathlib.Path, str]]
        path list to load plotter classes from.

    plotter_class: object
        plotter class

    Returns
    -------
    Dict
        A dict of BasePlotters.
    """
    plotters = dict()
    for path in paths:
        path_object = pathlib.Path(path)
        if not path_object.exists():
            raise OSError(f"path does not exist: {path_object.absolute()}")

        if path_object.name.endswith("tests"):
            return plotters

        for sub_path in path_object.iterdir():
            if sub_path.is_dir():
                sub_plotters = load_plotters_from_paths([sub_path], plotter_class)
                for a_plotter in sub_plotters:
                    plotters[a_plotter] = sub_plotters[a_plotter]
            elif sub_path.is_file():
                p = str(sub_path.absolute())
                file_name = sub_path.name
                if (
                        len(p) > 3
                        and p[-3:] == ".py"
                        and file_name[0:4] != "test"
                        and file_name != "__init__"
                        and p[0] != "."
                ):
                    mod = _load_module(sub_path)
                    for object_name in dir(mod):
                        an_object = getattr(mod, object_name)
                        if (
                                inspect.isclass(an_object)
                                and _is_subclass(an_object, plotter_class)
                                and an_object != plotter_class
                        ):
                            if an_object.plot_types is None:
                                continue
                            for a_plot_type in an_object.plot_types:
                                plotters[a_plot_type] = an_object
    return plotters


def _is_subclass(an_object, plotter_class: Union[Type[BasePlotter], Tuple[Type[BasePlotter]]]) -> bool:
    if not isinstance(plotter_class, tuple):
        plotter_class = (plotter_class, )
    for c in plotter_class:
        if issubclass(an_object, c):
            return True
    return False
