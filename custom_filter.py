from collections.abc import Iterable
from typing import Optional


def my_filter(function: Optional[callable], iterable_object: Iterable) -> list:
    """
    This function receive function or None and iterable and return new list which contains the value receive true in
    the function or if reveive None the values of items their value not equal to false.
    :param function: The function - receive item and return boolean.
    :param iterable_object: Iterable object to check its items.
    :return: the items receive true in the function or their value is true if None received instead of function.
    """
    new_list = []
    for value in iterable_object:
        if function:
            if function(value):
                new_list.append(value)
        else:
            if value:
                new_list.append(value)
    return new_list


if __name__ == "__main__":
    ages = [0, 1, 4, 10, 20, 35, 56, 84, 120]
    mature_ages_my_filter = my_filter(lambda value: value > 18, ages)
    print(tuple(mature_ages_my_filter))
