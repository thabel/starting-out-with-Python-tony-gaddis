import matplotlib.pyplot as plt

from startingPython.utility import read_file_lines


def main():
    labels = ('Rent', 'Gas', 'Food', 'Clothing', 'Car payment', 'Misc')
    sizes = [int(lines) for lines in read_file_lines("Expenses")]
    plt.pie(sizes, labels=labels)
    plt.show()


if __name__ == '__main__':
    main()
