from startingPython.utility import read_file_lines


def main():
    # average price per year
    years_data = computeData(yearsTools)
    months_data = computeData(monthTools)
    av_year, av_month = average(years_data), average(months_data)
    print("Year average ... ")
    display_averag(av_year)
    print("Month average ... ")
    display_averag(av_month)
    # utility function
    sorting_year_data(years_data)
    # then priting the lowers
    print("printing the lowerst price per year")
    display_highest_or_lowest(years_data)
    print("printing the hightest price per year")
    display_highest_or_lowest(years_data, lowest=False)


def display_highest_or_lowest(years_data, lowest=True):
    for year, list_of_tuples in years_data:
        if lowest:
            print(f"year : {year} date {list_of_tuples[0][0]} price {list_of_tuples[0][1]}")
        else:
            print(f"year : {year} date {list_of_tuples[-1][0]} price {list_of_tuples[-1][1]}")


def display_averag(list_of_tuples):
    for label, value in list_of_tuples:
        print(f"{label} ---- {value}")


def average(years_data):
    av_per_year = []
    for index, datas in enumerate(years_data):
        av_per_year.append([datas[0]])
        sum_list = [float(val[1]) for val in datas[1]]
        average = round(sum(sum_list) / len(sum_list), 3)
        av_per_year[index].append(average)
        av_per_year[index] = tuple(av_per_year[index])
    return av_per_year


def sorting_year_data(years_data):
    """this function will modify data"""
    for year, list_of_tuples in years_data:
        list_of_tuples.sort(key=lambda item: item[1])


def lines_contains_year(line, year):
    return year in line


def line_contains_month(line, month):
    return line.startswith(month)


yearsTools = (
    [str(year) for year in range(1993, 2014)],
    lines_contains_year,
)
monthTools = (
    [str(month).zfill(2) for month in range(1, 13)],
    line_contains_month,
)


def generate_text_file(file, reverse=False):
    list_of_lines = read_file_lines('GasPrices.txt')
    reformat_list = [line.replace("\n", "").split(':') for line in list_of_lines]
    reformat_list.sort(key=lambda item: item[1], reverse=reverse)
    reformat_list = [":".join(line) for line in reformat_list]
    reformat_list = "\n".join(reformat_list)
    with open(file, "w") as f:
        f.write(reformat_list)


def computeData(tupleTool):
    list_of_lines = read_file_lines('GasPrices.txt')
    # classer par année on construra une liste de tuple de cette facon
    # [(annee,[(date,prix),..])
    data = []
    list_of_initiator = tupleTool[0]
    for index, initiator in enumerate(list_of_initiator):
        data.append((initiator, []))
        for line in list_of_lines:
            line = line.replace('\n', '')
            if tupleTool[1](line, initiator):
                # acces year,[]
                data[index][1].append(tuple(line.split(':')))
    print(data[0])
    return data


if __name__ == '__main__':
    generate_text_file("GasPricesAsendingPrice.txt")
    generate_text_file("GasPricesDesendingPrice.txt", reverse=True)
