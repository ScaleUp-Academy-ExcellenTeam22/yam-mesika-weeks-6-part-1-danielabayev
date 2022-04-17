def full_names(first_names: list[str], last_names: list[str], min_length: int = 0) -> list[str]:
    """
    This function receive first and last names, make their first latter upper case and make all the combinations of the
    names. If min_length received the names returns will be the names their length is >= to min_length.
    :param first_names: List of the first names.
    :param last_names: List of the last names.
    :param min_length: Optional, the min_length of names.
    :return: List of the names.
    """
    first_names = [name.title() for name in first_names]
    last_names = [name.title() for name in last_names]
    full_name = [first + " " + last for first in first_names for last in last_names]
    full_name = [name for name in full_name if len(name) >= min_length]
    return full_name


if __name__ == "__main__":
    first_name = ['avi', 'moshe', 'yaakov']
    last_name = ['cohen', 'levi', 'mizrahi']
    print(full_names(first_name, last_name))
    print(full_names(first_name, last_name, 10))
