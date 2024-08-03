def rec_multiplication(a,b):
    if b==0:
        return 0
    return a + rec_multiplication(a,b-1)

print(rec_multiplication(7,4))