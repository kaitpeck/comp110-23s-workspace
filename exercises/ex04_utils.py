"""List Utility Functions."""

___name__ = 730314385


def all(num_list: list[int], num: int) -> bool:
    """Checks if all nums in the list match the indicated num."""
    cont: bool = True
    i: int = 0
    if len(num_list) == 0:
        cont = False
    while (cont is True) and (i < len(num_list)):
        if num_list[i] == num:
            i = i + 1
            cont = True
        elif num_list[i] != num:
            cont = False
    return cont


def max(num_list: list[int]) -> int:
    """Checks the highest number in a list."""
    i: int = 0
    highest: int = num_list[0]
    while i < len(num_list):
        if num_list[i] > highest:
            highest = num_list[i]
            i = i + 1
        else:
            i = i + 1
    return highest


def is_equal(first_list: list[int], sec_list: list[int]) -> bool:
    """Checks to see if the lists match."""
    if first_list == sec_list:
        return True
    else:
        return False