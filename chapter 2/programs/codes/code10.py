# 48 Cookies 
#* 1.5 cups of sugar
#* 1 cup of butter
#*2.75 cups of flour

# 48 cookies 1.5 cups of sugar
# 48 cookies 1 cup of butter
# 48 cookies of flour

# X*1.5/48 == Y cups of sugar

cookiesNum = int(input("Enter the number of cookies: "))
sugar = float(cookiesNum*1.5/48)
butter = float(cookiesNum*1/48)
flour = float(cookiesNum*2.75/48)

print("You will need ",sugar,"cup(s) of sugar")
print("You will need ",butter,"cup(s) of butter")
print("You will need ",flour,"cup(s) of flour")