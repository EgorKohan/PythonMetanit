import os.path


def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ") \
        .replace(",", " ") \
        .replace(".", " ") \
        .replace("?", " ") \
        .replace("!", " ") \
        .lower()

    words = text.split()
    words.sort()

    return words


def get_words_dict(words):
    words_dict = dict()
    for word in words:
        if word not in words_dict.keys():
            words_dict[word] = 1
        else:
            words_dict[word] = words_dict[word] + 1

    return words_dict


def main():
    filename = input("Input filename: ")
    if not os.path.exists(filename):
        print("Incorrect path!")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print(f"Count of words: {len(words)}")
        print(f"Unique words count: {len(words_dict)}")
        print(f"All words: ")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == "__main__":
    main()