def get_positive_numbers():
    numbers = input("enter the numbers:")
    numbers = numbers.split(",")
    numbers = [number for number in numbers if int(number) > 0]
    return numbers


if __name__ == "__main__":
    print(get_positive_numbers())
