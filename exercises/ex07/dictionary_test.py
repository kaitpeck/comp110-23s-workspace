"""Pytest for exercises 7: dictionary functions!"""

__author__ = "730314385"


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count

def test_invert_inversion() -> None:
    """Ensures the values are correctly inverted."""
    test_dict: dict[str, str] = {'alyssa': 'a', 'kris': 'k', 'charlotte': 'c'}
    invert_dict: dict[str, str] = {'a': 'alyssa', "k": 'kris', "c": 'charlotte'}
    assert invert(test_dict) == invert_dict


def test_invert_empty() -> None:
    """If a list is empty, there is nothing to invert."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_len() -> None:
    """Testing to ensure that the length of the list hasn't changed."""
    test_dict: dict[str, str] = {'alyssa': 'a', 'kris': 'k', 'charlotte': 'c'}
    assert len(invert(test_dict)) == len(test_dict)


def test_favcol_tie() -> None:
    """If there is a tie, the first encountered is the favorite."""
    test_dict: dict[str, str] = {'alyssa': 'blue', 'kris': 'green', 'charlotte': 'green'}
    assert favorite_color(test_dict) == 'green'


def test_favcol_one_value() -> None:
    """Ensures there is only one value returned."""
    test_dict: dict[str, str] = {'alyssa': 'blue', 'kris': 'green', 'charlotte': 'green'}
    assert len(favorite_color(test_dict)) == 1


def test_favcol_empty() -> None:
    """If there is an empty list, nothing is the favorite."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == {}


def test_count_first() -> None:
    """Ensures order hasn't changed."""
    test_list: list[str] = ["alyssa", "kris", "charlotte"]
    assert count(test_list)[0] == test_list[0]
    

def test_count_no_zeros() -> None:
    """Ensures there are no counts of zeros assigned."""
    test_list: list[str] = ["alyssa", "kris", "charlotte"]
    for key in count(test_list):
        assert count(test_list)[key] != 0 


def test_count_empty() -> None:
    """If there is an empty list, there is nothing to county."""
    test_list: list[str] = []
    assert count(test_list) == []