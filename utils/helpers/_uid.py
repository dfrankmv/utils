from ..std import *

def uid(size:int) -> str:
    """
    Generate a random alphanumeric string of the given length.

    >>> uid(5) # 'aZ4kP'
    >>> uid(8) # 'hD9gX1tB'
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=size))

if __name__ == "__main__":
    print(uid(5))
    print(uid(8))