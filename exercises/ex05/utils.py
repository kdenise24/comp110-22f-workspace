"""EX05 - `list` Utility Functions."""
__author__ = "730566062"


def only_evens(listof_ints: list[int]) -> (list[int]):
    """Given a list of ints, return the even ints, or return nothing at all."""
    i: int = 0 
    evens: int = []
    while i < len(listof_ints):
        if listof_ints[i] % 2 == 0:
            evens.append(listof_ints[i])
        i += 1
    return evens


def concat(firstlist: list[int], second_list: list[int]) -> (list[int]):
    """Given two lists of ints, a new list will be generated with the ints from the first list followed by the second list of ints."""
    i: int = 0
    endlist: list[int] = []
    while i < len(firstlist):     
        endlist.append(firstlist[i])
        i += 1
    idx: int = 0
    while idx < len(second_list):     
        endlist.append(second_list[idx])
        idx += 1
    return endlist


def sub(list: list[int], first_int: int, second_int: int) -> (list[int]):
    """Given a list and two ints, sub should generate a List which is a subset of the given list, between the specified start index and the end index -1."""
    a_list: list[int] = []
    if len(list) == 0:
        return []
    if first_int > len(list):
        return []
    if second_int <= 0:
        return []
    if first_int < 0:
        first_int = 0
    if second_int > len(list):
        second_int = len(list)
    while first_int != second_int:
        a_list.append(list[first_int])
        first_int += 1
    return a_list