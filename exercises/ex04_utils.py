"""EX04 - `list` Utility Functions"""
__author__ = "730566062"

def all(list_ofints: (list[int]), single: int):
    """given the list and the single int, returns a bool if they are equal"""
    i: int = 0
    if len(list_ofints) == 0:
        return False
    while i < len(list_ofints):
        if list_ofints[i] != single:
            return False
        i = i + 1
    return True


def max(input: list[int]) -> int:
    """given the lis, returns the max value/int"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        i: int = 0
        largest: int = input[0]
        while i < len(input):
            if largest < input[i]:
                largest = input[1]
            i = i + 1
        return largest


def is_equal(first_list: list[int], second_list: list[int]):
    """takes both lists and checks in they are equal to each other"""
    i: int = 0
    if len(first_list) != len(second_list):
        return False
    while i < len(first_list):
        if first_list[i] != second_list[i]:
            return False
        i = i + 1
    return True