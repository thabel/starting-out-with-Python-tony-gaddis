# deleting stduents record in file
import os
file = open("students.txt",'r')
name = file.readline()
search = 'Fabrice'
found = False
temp = open("temp.txt",'w')
while name != '':
    score = file.readline()

    if name.rstrip('\n') == search:
        found = True
    else:
        temp.write(name)
        temp.write(score)
    name = file.readline()
if found:
    print(search,"deleted successfully")
else:
    print(search,"not found in file")
temp.close()
file.close()
os.remove("students.txt")
os.rename("temp.txt","students.txt")
