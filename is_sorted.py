# File: is_sorted.py


def is_sorted(lst):
    """
    this function returns True is the given list is sorted
    :param lst: list of nums list((int)...)
    :return: bool
    """
    if lst != list(filter(lambda x: isinstance(x, int), lst)):
        return None
    if lst == sorted(lst):
        return True
    return False
