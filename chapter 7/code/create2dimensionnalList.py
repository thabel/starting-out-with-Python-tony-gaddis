#

def create2DList(rows,cols):
    list_ = []
    for row in range(rows):
        new_list = []
        for col in range(cols):
            new_list.append(0)
        list_.append(new_list)

A = create2DList(3,3)

print(A)




