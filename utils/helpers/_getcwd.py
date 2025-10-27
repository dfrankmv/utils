from ..std import *

def getcwd() -> str:
    """
    Returns the absolute path of the current working directory.
    This is typically the directory from which the Python script is run.

    >>> getcwd() # "/home/user/workspace/binance"
    """
    return os.path.abspath(os.getcwd())