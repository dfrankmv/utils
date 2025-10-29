def make_hashable(value):
    """
    Recursively converts a Python object into a hashable equivalent.

    This function is useful for making objects (such as dictionaries, lists, or sets)
    usable as keys in dictionaries or as elements of sets.

    >>> make_hashable({'a': [1, 2], 'b': {'x', 'y'}})
    frozenset({('a', (1, 2)), ('b', frozenset({'y', 'x'}))})

    >>> my_dict = {}
    >>> my_dict[make_hashable({'a': [1, 2]})] = "value"
    >>> my_dict
    {frozenset({('a', (1, 2))}): 'value'}
    """
    if isinstance(value, dict):
        return frozenset((k, make_hashable(v)) for k, v in value.items())
    elif isinstance(value, (list, tuple)):
        return tuple(make_hashable(v) for v in value)
    elif isinstance(value, set):
        return frozenset(make_hashable(v) for v in value)
    else:
        return value