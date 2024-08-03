# This program displays a sales chart.
import matplotlib.pyplot as plt

from startingPython.utility import read_file_lines


def main():
    fig, ax = plt.subplots()

    counts = [int(line) for line in read_file_lines("1994_Weekly_ Gas_Averages.txt")]
    fruits = [i for i in range(len(counts))]
    # Adjust spacing between bars
    bar_width = 0.5  # Adjust the width of the bars
    bar_spacing = 0.2  # Adjust the spacing between the bars
    ax.bar(fruits, counts)
    plt.xticks(rotation=90)
    # Adjust x-axis limits and spacing between bars
    plt.xlim(min(fruits) - (bar_width + bar_spacing), max(fruits) + (bar_width + bar_spacing))
    ax.set_ylabel('prices')
    ax.set_title('Weeks')
    ax.legend(title='Gaz average')

    plt.show()


# Call the main function.
if __name__ == '__main__':
    main()
