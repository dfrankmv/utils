from ..std import *

class EnumWithNoneMeta(EnumMeta):
    def __call__(cls, value, *args, **kwargs):
        if value is None:
            return None
        try:
            return super().__call__(value, *args, **kwargs)
        except ValueError:
            return None

    def __getitem__(cls, item):
        if item is None:
            return None
        return super().__getitem__(item)

class BINARY(int, Enum, metaclass=EnumWithNoneMeta):
    """
    Integer-based Enum for binary states (1 and -1) that safely returns None for invalid or None values.
    Supports negation.

    Example:
    >>> class DIR(BINARY):
    ...     UP = -1
    ...     DN = 1
    ...
    >>> -DIR.UP
    <DIR.DN: -1>
    """

    def __str__(self): return self.name
    def __int__(self): return self.value

    @classmethod
    def get(cls, key):
        if key is None:
            return None
        return cls.__getitem__(key)

    def __neg__(self):
        return self.__class__(-self.value)

    def __hash__(self):
        return hash(self.value)
    
if __name__ == "__main__":
    class DIR(BINARY):
        UP = 1
        DN = -1
    print(-DIR.UP) # DIR.DN