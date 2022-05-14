import string
from collections.abc import Generator


def words(text: str) -> Generator[str]:
    """
    This is generator receive text, split it to the word without the punctuations.
    :param text: The text.
    :return: The words without punctuations.
    """
    text = text.split()
    for word in text:
        for character in string.punctuation:
            the_word = word.replace(character, '')
        yield the_word


def count_words(text: str) -> dict:
    """
    This function receive text and return dictionary with the words and their length.
    :param text: The text to make dictionary from.
    :return: Dictionary of word and its length.
    """
    return {word: len(word) for word in words(text)}


if __name__ == "__main__":
    my_text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(count_words(my_text))
