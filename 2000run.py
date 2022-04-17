import time
from typing import Optional


def timer(function: Optional[callable], *args, **kwargs) -> float:
    """
    This function receive function and parameters and calculate the time the function that to do with these parameters.
    :param function: The function to make.
    :param args: Parameters to the function.
    :param kwargs: Parameters to the function.
    :return: The time take to the function to run.
    """
    start = time.time()
    function(*args, **kwargs)
    end = time.time()
    return end - start


if __name__ == "__main__":
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
