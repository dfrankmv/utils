from ..std import *

def current_datetime(format:str='%Y%m%d%H%M%S') -> str:
    """
    Returns the current date and time as a formatted string.

    >>> now() # "20230819212350"
    """
    return datetime.datetime.now().strftime(format)

if __name__ == "__main__":
    print(current_datetime())