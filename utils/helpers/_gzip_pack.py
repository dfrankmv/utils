from ..std import *

from ._mkdir import *

def gzip_pack(data, filename_gz:str) -> None:
    """
    Compresses a Python object by serializing it to JSON and saving it into a gzip file.

    >>> x = "test value"
    >>> gzip_pack(x, "test.gz") # New file test.gz created
    >>> gzip_pack(x, "temp/demo/test.gz") # Parent dirs are created if don't exist
    """
    dir_path = os.path.dirname(filename_gz)
    if dir_path:
        mkdir(dir_path)
    with gzip.open(filename_gz, "wt", encoding="utf-8") as f:
        json.dump(data, f)

if __name__ == "__main__":
    x = "test value"
    gzip_pack(x, "test.gz")
    gzip_pack(x, "temp/demo/test.gz")