#
dict_of_words_line = {}
def main():
    with open("Kennedy.txt","r") as f:
        for num,line in enumerate(f):
            line = line.rstrip()
            for word in line.split():
                if word in dict_of_words_line:
                    dict_of_words_line[word].add(str(num+1))
                else:
                    dict_of_words_line[word] = set(str(num+1))
    with open("index.txt","w") as f:
        for k,v in sorted(dict_of_words_line.items(),key=lambda item:item[0]):
            f.write(f"{k}: {' '.join(v)}\n")

    print(dict_of_words_line)


if __name__ == '__main__':
    main()
