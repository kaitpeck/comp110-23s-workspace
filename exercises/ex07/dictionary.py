"""Exercise 07: Dictionary Functions!"""

__author__ = "730314385"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Return a dictionary that inverts the keys and values."""
    dictionary = {value: key for key, value in dictionary.items()}
    return dictionary


def favorite_color(inp_dict: dict[str, str]) -> str:
    """Returns a str which is the color that appears most frequently."""
    #  If there is a tie, return the color that appeared first!
    color_dict: count(dict[str, int]) = {}
    color_list: list[str] = []
    for keys in inp_dict:
        color_list.append(inp_dict[keys])
    i: int = 0
    favorite: str = color_dict[i + 1]
    if inp_dict == {}:
        return None
    while i < len(color_dict):
        if color_dict[i + 1] > color_dict[i]:
            favorite = color_dict[i + 1]
        else:
            favorite = color_dict[i]
    return favorite


def count(inp_list: list[str]) -> dict[str, int]:
    """Each key is a unique value in the list and each value is the count of appearances of the value."""
    count_dict: dict[str, int] = {}
    i: int = 0
    name: str = inp_list[i]
    while i < len(inp_list):
        if name in count_dict:
            count_dict[name] += 1
        else:
            count_dict[name] = 1
        i += 1
    return count_dict
