from ..std import *

def current_millis() -> int:
    """ Returns the current time in milliseconds since the Unix epoch.
    
    >>> current_millis() # 1754764210930
    """
    return int(time.time() * 1000)

if __name__ == "__main__":
    print(current_millis())