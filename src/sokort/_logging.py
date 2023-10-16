import logging
from typing import Union


def get_logger(name='main'):
    try:
        import loguru
        logger = loguru.logger
    except ImportError:
        logger = logging.getLogger(name)
    return logger


def convert_verbose(verbose: Union[bool, int]):
    v = verbose
    if isinstance(v, bool):
        v = 1 if v else 0
    return v
