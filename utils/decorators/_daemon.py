from ..helpers import *

P = ParamSpec('P')
"""
P is a ParamSpec used to capture the exact parameter signature of the decorated 
function, so that editor tooltips and autocompletion (e.g., in VSCode) preserve the 
original argument names and types.
"""

@overload
def daemon(func: Callable[P, Any]) -> Callable[P, Thread]:
    ...
    
def daemon(func: Callable[P, Any]) -> Callable[P, Thread]:
    """
    Decorator that runs the decorated function in a new thread.

    When this decorator is applied to a function, calling that function will execute it
    asynchronously in a separate thread. The decorator returns the Thread object, 
    allowing you to manage the thread explicitly if needed.

    Parameters
    ----------
    func : Callable
        The function to be run in a separate thread.

    Returns
    -------
    Callable[..., threading.Thread]
        A function that, when invoked, starts the original function in a thread and 
        returns the started Thread object.

    Example
    -------
    >>> import time
    >>> @daemon
    ... def work():
    ...     print("Thread started")
    ...     time.sleep(1)
    ...     print("Thread finished")
    ...
    >>> th = work()
    >>> print("Main continues")
    >>> th.join()  # Wait for thread to complete
    """
    
    @wraps(func)
    def wrapper(*args, **kwargs) -> Thread:
        def thread_target():
            func(*args, **kwargs)
        thread = Thread(target=thread_target, name=f"{func.__name__}_{str(id(func))[-4:]}", daemon=True)
        thread.start()
        return thread
    
    return wrapper
