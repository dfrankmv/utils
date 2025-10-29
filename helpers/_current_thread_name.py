from ..std import *

def current_thread_name():
    """
    Retrieves the name of the current thread
    """
    return threading.current_thread().name