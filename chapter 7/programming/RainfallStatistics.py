"""
Design a program that lets the user enter the total rainfall for each of 12 months into a
list. The program should calculate and display the total rainfall for the year, the average
monthly rainfall, the months with the highest and lowest amounts.
"""

rail_fool_list = list()
MONTHS = ["January", "February", "March", "April",
          "May", "June", "July", "August",
          "September", "October", "November", "December"]
for i in range(12):
    a = float(input("enter rainfall for " + MONTHS[i] + " : "))
    rail_fool_list.append(a)

print("Total = ", sum(rail_fool_list))
print("Average = ", round(sum(rail_fool_list) / len(rail_fool_list), 2))


# finding _minimum rail fall month
def all_index_of_valueVo(rail_fool_list):
    min_r = min(rail_fool_list)
    all_min_index = [rail_fool_list.index(min_r)]
    #
    print(min_r)
    start = all_min_index[-1] + 1
    print(start)
    while rail_fool_list[start:].count(min_r):
        if start == len(rail_fool_list) - 1:
            break
        index = rail_fool_list[start:].index(min_r) + all_min_index[-1] + 1
        all_min_index.append(index)
        start = all_min_index[-1] + 1
    print(all_min_index)


def all_index_of_value(rail_fool_list, min_r=0):
    if min_r == 0:
        min_r = min(rail_fool_list)
    else:
        min_r = max(rail_fool_list)
    all_index_of_value = list()
    for i in range(len(rail_fool_list)):
        if rail_fool_list[i] == min_r:
            all_index_of_value.append(i)
    return all_index_of_value


print("Months with highest amount: ", [MONTHS[i] for i in all_index_of_value(rail_fool_list, min_r=1)])
print("Months with lower amount: ", [MONTHS[i] for i in all_index_of_value(rail_fool_list)])

# for list think about for i in range
