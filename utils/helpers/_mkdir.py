from ..std import *

def mkdir(path:str) -> str:
    """
    Creates a directory (and any necessary parent directories) if it does not exist.

    >>> mkdir("example_dir")
    'example_dir'
    >>> os.path.isdir("example_dir")
    True
    """
    os.makedirs(path, exist_ok=True)
    return path