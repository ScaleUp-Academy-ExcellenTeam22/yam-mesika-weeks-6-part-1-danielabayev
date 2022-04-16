def words_length(line: str) -> list[int]:
    words = line.split()
    words_length_lst = [len(word) for word in words]
    return words_length_lst


if __name__ == "__main__":
    print(words_length("Toto, I've a feeling we're not in Kansas anymore"))
