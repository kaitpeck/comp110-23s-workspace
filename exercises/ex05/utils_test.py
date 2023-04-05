"""Unit test for utils ex05"""

__author__ = "730314385"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat

"""even tests"""
def test_even() -> None:
    """all values in new list are even"""
    test_list: list[int] = [1,2,3,4]
    assert only_evens(test_list) == [2,4]

def test_int() -> None:
    """all values must be integers"""
    test_list: list[int] = [1,2,3,4]
    for values in test_list:
        assert type(values) == int

def test_no_modify() -> None:
    """cannot modify reference list"""
    test_list: list[int] = [1,2,3,4]
    assert test_list == test_list



"""concat tests"""
def test_empty_first() -> None:
    """first list plus empty list equals first list"""
    test_f_list: list[int] = [1,2,3,4]
    test_s_list: list[int] = []
    assert concat(test_f_list,test_s_list) == [1,2,3,4]


def test_mutate_first() -> None:
    """no modification to first list"""
    test_f_list: list[int] = [1,2,3,4]
    test_s_list: list[int] = []
    assert concat(test_f_list,test_s_list) == concat(test_f_list,test_s_list)

def test_mutate_sec() -> None:
    """no modification to second list"""
    test_f_list: list[int] = []
    test_s_list: list[int] = [2,3,4,5]
    assert concat(test_f_list,test_s_list) == concat(test_f_list,test_s_list)



"""sub tests"""
def test_empty_list() -> None:
    """empty list returns empty list"""
    test_list: list[int] = []
    test_f_int: int = 0
    test_s_int: int = 3
    assert sub(test_list, test_f_int, test_s_int) == []
  

def test_start_negative() -> None:
    """start from beginning if start index is negative"""
    test_list: list[int] = [1,2,3,4]
    test_f_int: int = -1
    test_s_int: int = 4
    assert sub(test_list, test_f_int, test_s_int) == [1,2,3,4]

def test_bigger_end() -> None:
    """if end index is greater than length of list, end with the end of the list"""
    test_list: list[int] = [1,2,3,4]
    test_f_int: int = 0
    test_s_int: int = 7
    assert sub(test_list, test_f_int, test_s_int) == [1,2,3,4]