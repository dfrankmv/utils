import threading
import contextlib

@contextlib.contextmanager
def run_until_interrupt():
    """
    Context manager that keeps a process running until the user manually stops it with Ctrl+C.

    This is useful for keeping background tasks, servers, or listeners active 
    without exiting immediately after startup. The code inside the `with` block 
    runs once, and after it completes, the context will block until a KeyboardInterrupt occurs.

    Behavior
    --------
    - Executes the code inside the `with` block.
    - After that, it waits indefinitely.
    - When the user presses Ctrl+C, a KeyboardInterrupt is caught, 
      and a message is printed indicating the block has ended.

    Example
    -------
    >>> from time import sleep
    >>> with run_until_interrupt():
    ...     print("Running... press Ctrl+C to stop.")
    ...     sleep(1)
    ...     print("Setup complete, now waiting.")
    Running... press Ctrl+C to stop.
    Setup complete, now waiting.
    ^C
    """
    stop_event = threading.Event()
    try:
        yield  # HERE THE CODE INSIDE THE "WITH" BLOCK WILL BE EXECUTED
        stop_event.wait()  # BLOCKS AFTER THE EXECUTION OF THE BLOCK
    except KeyboardInterrupt:
        pass