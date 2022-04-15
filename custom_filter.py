from collections.abc import Iterable
from typing import Optional


def my_filter(function: Optional[callable], iterable_value: Iterable) -> list:
    new_list = []
    for value in iterable_value:
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
