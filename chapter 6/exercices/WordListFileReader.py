"""
This exercise assumes you have completed the Programming Exercise 7, Word List File
Writer. Write another program that reads the words from the file and displays the following data:
•	 The number of words in the file.
•	 The longest word in the file.
•	 The average length of all of the words in the file.
"""
file_name = "wordlist.txt"
try:
    with open(file_name, "r") as file:
        a = 0;
        i = 0
        long_word = ""
        for line in file:
            for word in line.split():
                if (len(word) > len(long_word)):
                    long_word = word
                a += len(word)
                i += 1
        print("the sum of words is =", i)
        print("the average is =", round(a / i ,2))
        print("the long word is =",long_word)
except:
    print("Error when opening file!")
