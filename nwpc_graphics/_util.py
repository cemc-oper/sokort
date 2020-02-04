import pathlib
import importlib.util
import sys


def _load_module(file_path: pathlib.Path):
    """Load module in file.
    """
    module_name = file_path.stem
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _get_load_env_script():
    return pathlib.Path(pathlib.Path(__file__).parent, "load_env.sh")
