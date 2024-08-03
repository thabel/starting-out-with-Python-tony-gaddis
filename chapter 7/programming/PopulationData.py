"""
If you have downloaded the source code you will find a file named USPopulation.txt
in the Chapter 07 folder. The file contains the midyear population of the United States, in
thousands, during the years 1950 through 1990. The first line in the file contains the population for 1950, the second
line contains the population for 1951, and so forth.
Write a program that reads the file’s contents into a list. The program should display the
following data:
•	 The average annual change in population during the time period
•	 The year with the greatest increase in population during the time period
•	 The year with the smallest increase in population during the time period
"""


def main():
    try:
        SHIFT = 1950
        with open("USPopulation.txt", "r") as file:
            list_of_general = []
            for line in file:
                list_of_general.append(int(line.rstrip()))
            print("The average ", "." * 10, round(sum(list_of_general) / len(list_of_general), 2))
            print("The year with the greatest increase in population during ",
                  list_of_general.index(max(list_of_general)) + SHIFT)
            print("The year with the smallest increase in population during ",
                  list_of_general.index(min(list_of_general)) + SHIFT)
    except FileNotFoundError:
        print("File not found !")


if __name__ == '__main__':
    main()
