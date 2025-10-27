from ..std import *

def gzip_unpack(filename_gz:str) -> Any:
    """
    Decompresses a gzip file containing JSON data and deserializes it to a Python object.

    >>> x = gzip_unpack("temp/demo/test.gz") # "test value"
    """
    with gzip.open(filename_gz, "rt", encoding="utf-8") as f:
        return json.load(f)
    
if __name__ == "__main__":
    z = gzip_unpack("temp/demo/test.gz")
    print(z)