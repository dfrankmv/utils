def what_comes_after_last(text:str, sep:str):
    """ Returns the substring that appears after the last occurrence of `sep` in `text`.

    >>> what_comes_after_last("path/to/my/file.txt", "/") # 'file.txt'
    >>> what_comes_after_last("one-two-three", "-") # 'three'
    >>> what_comes_after_last("abcXYZdefXYZghi", "XYZ") # 'ghi'
    >>> what_comes_after_last("hello", "z") # 'hello'
    """
    idx = text.rfind(sep)
    if idx == -1:
        return text
    return text[idx + len(sep):]

if __name__ == "__main__":
    print(what_comes_after_last("path/to/my/file.txt", "/")) # 'file.txt'
    print(what_comes_after_last("one-two-three", "-")) # 'three'
    print(what_comes_after_last("abcXYZdefXYZghi", "XYZ")) # 'ghi'
    print(what_comes_after_last("hello", "world")) # 'hello'