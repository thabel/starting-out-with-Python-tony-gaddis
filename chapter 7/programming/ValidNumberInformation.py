
def is_in_range(n):
    return n>=0 and n<=100

valid_numbers=[]
# for n in numbers:
#     if is_in_range(n):
#         valid_numbers.append(n)
#
# print(valid_numbers)#[74, 19, 20, 67, 77, 38]
numbers = [74, 19, 105, 20,-2, 67, 77, 124,-45, 38]
valid_numbers = list(filter(lambda x:is_in_range(x),numbers))
print(valid_numbers)
