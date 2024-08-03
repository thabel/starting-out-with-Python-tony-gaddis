from startingPython.utility import read_file_lines


def main():
    list_of_sentences = read_file_lines("text.txt")
    number_of_sentence = len(list_of_sentences)
    for index,line in enumerate(list_of_sentences):
        word_list = line.split()
        print(f"average of sentence {index+1} = {round(len(word_list)/number_of_sentence,2)} word")



if __name__ == '__main__':
    main()
