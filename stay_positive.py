def get_positive_numbers() -> list:
    """
    This function read numbers from the user separate by comma and return the positive numbers.
    :return: the positive numbers.
    """
    numbers = input("enter the numbers:")
    numbers = numbers.split(",")
    numbers = [number for number in numbers if int(number) > 0]
    return numbers


if __name__ == "__main__":
    print(get_positive_numbers())
