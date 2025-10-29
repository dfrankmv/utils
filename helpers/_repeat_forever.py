from ..std import *

def repeat_forever(func:Callable, every_secs:float) -> None:
    """
    Repeatedly executes a function at a fixed time interval.

    >>> def hello():
    ...     print("Hello")
    >>> # In practice, press Ctrl+C to stop it.
    >>> repeat_forever(hello, 1.0)
    """
    if every_secs <= 0:
        raise ValueError("`every_secs` must be greater than 0.")

    try:
        while True:
            try:
                func()
            except Exception as e:
                print(f"Error in repeat_forever: {e}")
            finally:
                time.sleep(every_secs)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    def say_hi():
        print("Hi")

    repeat_forever(say_hi, 2.0)