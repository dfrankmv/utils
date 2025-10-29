from ..std import *

def camel2snake(camel:str) -> str:
    """ Converts a string from camelCase or PascalCase to snake_case.

    >>> camel2snake("camelCaseExample") # camel_case_example
    >>> camel2snake("HTMLParser") # html_parser
    >>> camel2snake("userID") # user_id
    """
    camel = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', camel)
    camel = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel)
    return camel.lower()

if __name__ == "__main__":
    print(camel2snake("camelCaseExample")) # camel_case_example
    print(camel2snake("PascalCaseExample")) # pascal_case_example
    print(camel2snake("already_snake_case")) # already_snake_case
    print(camel2snake("HTMLParser")) # html_parser
    print(camel2snake("userID")) # user_id