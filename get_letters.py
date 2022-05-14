def get_letters() -> list[str]:
    """
    This function return all the letters lowercase and uppercase using list comprehension.
    :return: List of the letters.
    """
    return [chr(letter) for letter in range(ord("a"), ord("z") + 1)] + [chr(letter) for letter in range(ord("A"), ord("Z") + 1)]


if __name__ == "__main__":
    print(get_letters())
