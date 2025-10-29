from ..std import *
from ._urlencode import *

def hmac_sha256(dct:dict, key:str) -> str:
    """ Generate an HMAC-SHA256 signature for the given data and key.

    >>> hmac_sha256({"param1":"value1", "param2":"value2"}, "secret")
    # '10b123870c7d3279d8c3c12748b7b73f5e2a2ba39b7ad93d8d010a9608ae372d'
    """
        
    if not isinstance(dct, dict):
        raise TypeError("data must be a dictionary")
    if not isinstance(key, str):
        raise TypeError(f"key '{key}' must be a string")

    dct_encoded = urlencode(dct).encode()
    key_encoded = key.encode()
    
    return hmac.new(key_encoded, dct_encoded, hashlib.sha256).hexdigest()

if __name__ == "__main__":
    data = {
        "param1": "value1",
        "param2": "value2"
    }
    print(hmac_sha256(data, "secret"))    # '10b123870c7d3279d8c3c12748b7b73f5e2a2ba39b7ad93d8d010a9608ae372d'