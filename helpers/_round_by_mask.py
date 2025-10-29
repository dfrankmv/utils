from ..std import *

def round_by_mask(num:float, mask:str) -> int | float:
    """
    Rounds the given `num` to the nearest multiple of the specified `mask`.
    Ensures that the `mask` is a power of 10 (e.g., 1, 0.1, 0.01, 10, 100, etc.).

    >>> round_to_factor(123.456, "1")
    123
    >>> round_to_factor(123.456, "0.1")
    123.5
    >>> round_to_factor(123.456, "0.01")
    123.46
    >>> round_to_factor(123.456, "10")
    120
    """
    factor = float(mask)

    if factor <= 0 or math.log10(factor) % 1 != 0:
        raise ValueError("Factor must be a power of 10 (e.g., 1, 0.1, 0.01, 10, 100, etc.)")

    if factor < 1:
        decs = len(mask.split(".")[1].rstrip("0"))
    else:
        decs = 0
    
    rounded = round(round(num / factor) * factor, decs)
    
    if rounded.is_integer():
        return int(rounded)
    return rounded

if __name__ == "__main__":
    print(round_by_mask(123.456, "1"))
    print(round_by_mask(123.456, "0.1"))
    print(round_by_mask(123.456, "0.01"))
    print(round_by_mask(123.456, "10"))

    