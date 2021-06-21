import logging


def get_logger(name='main'):
    try:
        import loguru
        logger = loguru.logger
    except ImportError:
        logger = logging.getLogger(name)
    return logger
