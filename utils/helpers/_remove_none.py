def remove_none(dct:dict) -> dict:
    """
    Removes all items with `None` values from the given dictionary.

    >>> remove_none({"a":"A", "n":None, "b":"B"}) 
    # {"a":"A", "b":"B"}
    """
    return {} if dct is None else {k: v for k, v in dct.items() if v is not None}

if __name__ == "__main__":
    print(remove_none({
        "a": "A",
        "n": None,
        "b": "B",
    })) # {'a':'A', 'b':'B'}