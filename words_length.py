def words_length(line: str) -> list[int]:
    """
    This function receive line, split to words (including punctuation) and return list of the words length.
    :param line: The line to split to words and check their length.
    :return: List of the length of the words.
    """
    words = line.split()
    return [len(word) for word in words]


if __name__ == "__main__":
    print(words_length("Toto, I've a feeling we're not in Kansas anymore"))
