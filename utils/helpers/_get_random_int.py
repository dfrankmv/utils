from ..std import *

def random_int(digits:int):
    """
    Generates a random integer with the specified number of digits.

    >>> random_int(3) # 238
    >>> random_int(5) # 28584
    """
    if not isinstance(digits, int) or digits < 1:
        raise ValueError("'digits' should be an integer greater than 0.")
    
    return random.randint(10**(digits-1), 10**digits - 1)

if __name__ == "__main__":
    print(random_int(3))  # 238
    print(random_int(5))  # 28584