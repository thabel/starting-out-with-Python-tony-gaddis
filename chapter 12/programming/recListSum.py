def recSum(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + recSum(array[1:])
    
arr = [i for i in range(5)]
print(arr)
print(recSum(arr))