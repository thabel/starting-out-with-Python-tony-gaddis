import string

from startingPython.utility import unique_words_of_file


def main():
    words = unique_words_of_file("text.txt")
    print(words)


if __name__ == '__main__':
    main()
