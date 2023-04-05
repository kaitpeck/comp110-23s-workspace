"""Practicing list utility functions."""

__author__  = "730314385"

def only_evens(num_list: list[int]) -> list[int]:
    """Returning only even values in a list"""
    for value in num_list:
        if (value % 2) != 0:
            num_list.pop(value)
    return num_list

def concat(f_list: list[int], s_list: list[int]) -> list[int]:
    """returning list containing elements of both first and second list"""
    total_list: list[int] = []
    for values in f_list:
        total_list.append(values)
    for entries in s_list:
        total_list.append(entries)
    return total_list


def sub(a_list: list[int], num1: int, num2: int) -> list[int]:
    """generate a list which is a subset of a given list between the specified start index and end index -1"""
    sub_list: list[int] = []
    begin: int = ()
    end: int = ()
    if num1 < 0:
        begin = 0
    else:
        begin = num1
    if num2 > len(sub_list):
        end = len(sub_list) - 1
    else:
        end = num2
    if (len(a_list) == 0) or (num1 >= len(a_list)) or (num2 <= 0):
        return []
    for values in range(begin,end):
        new_list: list[int] = a_list[values]
        return new_list