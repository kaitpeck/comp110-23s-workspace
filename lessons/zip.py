"""Challenge Question 04."""

def zip(string: list[str], integer: list[int]) -> dict[str,int]:
    """produce a dict w/ keys strs and values at the same idx of ints"""
    inventory: dict[str,int] = {}
    if (len(string) != len(integer)) or (len(string) == 0) or (len(integer) == 0):
        return {}
    else:
        idx: int = 0
        while idx < len(string):
            inventory[string[idx]] = integer[idx]
            idx += 1
        return inventory

string: list[str] = ("apple", "banana", "orange")
integer: list[int] = (1,2,3)
print(zip(string,integer))
