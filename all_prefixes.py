# File: all_prefixes.py


def all_prefixes(string):
    """
    Generates a set of all possible sub-strings, which starts with the first
    letter of given string.
    A string shouldn't contain spaces.
    :param string: (str)
    :return: (set)
    """
    if not isinstance(string, str):
        return None
    if " " in string:
        return None
    string = string.lower()
    first_letter = string[0]
    prefixes = set()
    while first_letter in string:
        index = string.find(first_letter)
        lst = list(string)[index:]
        string = "".join(lst)
        for i in range(0, len(string)+1):
            prefixes.add(string[0:i+1])
        lst = list(string)
        lst.remove(first_letter)
        string = "".join(lst)
    return prefixes
