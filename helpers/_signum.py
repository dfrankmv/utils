def signum(val:float) -> int:
    """
    Returns the sign (+1 or -1) of a given number.

    >>> signum(10) # 1
    >>> signum(0) # 1
    >>> signum(-10) # -1
    >>> signum("a") # TypeError: Input must be a number
    """
    if not isinstance(val, (int, float)):
        raise TypeError("Input must be a number (int or float)")

    return 1 if val >= 0 else -1

if __name__ == "__main__":
    print(signum(10))
    print(signum(0))
    print(signum(-10))