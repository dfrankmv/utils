from ..std import *

def print_to_json(filepath_json:str, data:dict) -> None:
    """Saves a Python dictionary to a JSON file with pretty formatting.

    >>> print_to_json("test.json", {"a":"A", "b":"B"}) # Creates a new `test.json` file with the `data` content indented
    """
    if not isinstance(data, dict):
        raise ValueError(f"`data` must be a `dict`")
    
    if not filepath_json.endswith(".json"):
        raise ValueError(f"`filepath_json` must have `.json` extension")

    if "/" in filepath_json:
        os.makedirs(os.path.dirname(filepath_json), exist_ok=True)

    with open(filepath_json, "w") as f: 
        json.dump(data, f, indent=4)