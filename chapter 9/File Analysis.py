from startingPython.utility import unique_words_of_file


def main():
    v1_unique_words = unique_words_of_file("fileV1.txt")
    v2_unique_words = unique_words_of_file("fileV2.txt")

    # It should display a list of all the unique words contained in both files.
    result = v1_unique_words.union(v2_unique_words)
    print(f"list of all the unique words contained in both files\n {result}")
    # It should display a list of the words that appear in both files.
    result = v1_unique_words.intersection(v2_unique_words)
    print(f"list of the words that appear in both files \n{result}")
    # It should display a list of the words that appear in
    # the first file but not the second.
    result = v1_unique_words.difference(v2_unique_words)
    print("list of the words that appear in the first file but not the second\n"
          f"{result}")
    # It should display a list of the words that appear in
    # the second file but not the first
    result = v2_unique_words.difference(v1_unique_words)
    print("list of the words that appear in the second file but not the first"
          f"{result}")
    # It should display a list of the words that appear in either the first or second file, but not
    # both.
    result = v1_unique_words.symmetric_difference(v2_unique_words)
    print("list of the words that appear in either the "
          f"first or second file, but  not both {result}")


if __name__ == '__main__':
    main()
