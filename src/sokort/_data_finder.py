from pathlib import Path


def find_local_file(
        data_type,
        **kwargs
) -> Path or None:
    """
    Find CEMC Operating Systems data using ``reki`` package's ``find_local_file`` function.

    Parameters
    ----------
    data_type
    kwargs

    Returns
    -------
    Path or None
        local data file path, or None if not found.
    """
    from reki.data_finder import find_local_file
    return find_local_file(
        data_type,
        **kwargs
    )
