from ..std import *

def list_files(dirpath:str, file_extension:str='*') -> List[str]:
    """ 
    Lists all files with a specified extension in the given directory and returns their absolute paths.
    If no extension is provided, it returns all files in the directory.

    >>> list_files('/tmp', '.py')
    ['/tmp/example.py', '/tmp/test.py']
    """
    dir_path = Path(dirpath)
    
    if not dir_path.is_dir():
        raise FileNotFoundError(f"The directory {dir_path} does not exist.")
    
    if file_extension == '*':
        files = [f.resolve().as_posix() for f in dir_path.iterdir() if f.is_file()]
    else:
        files = [f.resolve().as_posix() for f in dir_path.glob(f'*{file_extension}') if f.is_file()]

    return sorted(files)

if __name__ == "__main__":
    print(list_files(".", ".py"))