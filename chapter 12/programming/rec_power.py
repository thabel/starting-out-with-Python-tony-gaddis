def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
    


assert power(2,3) == pow(2,3)
assert power(7,2) == pow(7,2)
assert  power(4,5) == pow(4,5)

print(power(3,3))