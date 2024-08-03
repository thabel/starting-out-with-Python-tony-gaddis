def large(array:list[int]):
    if len(array) == 1:
        return array[0]
    else:
        res = large(array[1:])
        if array[0] > res:
            return array[0]
        else:
            return res



print(large([3,4,50,8,10,0,7]))