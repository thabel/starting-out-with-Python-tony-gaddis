def print_element_and_index(L):
    print('*' * 20)
    for i in range(0, len(L)):
        print(L[i], '....... index ......... ', i)
    print('*' * 20)


L = list(range(2, 5))

print_element_and_index(L)
L.insert(-1, 1000)
print_element_and_index(L)
