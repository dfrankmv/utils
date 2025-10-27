from ..std import *

def urlencode(data:dict) -> str:
    """Encodes a dictionary into a URL query string, converting boolean values to 'true' or 'false', and omitting keys with None values.

    >>> urlencode({'active': True, 'count': 10, 'verbose': False, 'empty': None}) 
    # 'active=true&count=10&verbose=false'
    """
    return urllib.parse.urlencode({
        k: "true" if v is True else "false" if v is False else v
        for k, v in data.items() if v is not None
    })

if __name__ == "__main__":
    params = {
        "name": "Alice",
        "age": None,
        "city": "Wonderland",
        "is_active": False
    }
    print(urlencode(params)) # name=Alice&city=Wonderland&is_active=false