from pathlib import Path


def find_local_file(
        data_type,
        **kwargs
) -> Path or None:
    """
    Find NWPC Operation Systems data using ``nwpc-data`` package.
    Parameters
    ----------
    data_type
    kwargs

    Returns
    -------

    """
    from reki.data_finder import find_local_file
    return find_local_file(
        data_type,
        **kwargs
    )
