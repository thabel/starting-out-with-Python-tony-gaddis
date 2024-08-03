"""
Write a program that asks the user for his or her name, then asks the user to enter a sentence that describes himself or herself. Here is an example of the program’s screen:
Enter your name: Julie Taylor Enter
Describe yourself: I am a computer science major, a member of the
Jazz club, and I hope to work as a mobile app developer after I
graduate. Enter
Once the user has entered the requested input, the program should create an HTML file,
containing the input, for a simple Web page. Here is an example of the HTML content,
using the sample input previously shown:
<html>
<head>
</head>
<body>
 <center>
 <h1>Julie Taylor</h1>
 </center>
 <hr />
 I am a computer science major, a member of the Jazz club,
 and I hope to work as a mobile app developer after I graduate.
 <hr />
</body>
</html>
"""

file_name = "personnalPage.html"

try:
    with open(file_name,"w") as file:
        name = input("Enter your name:")
        desc = input("Describe yourself: ")

        file.write("""
        <html>
<head>
</head>
<body>
 <center>
 <h1>{namer}</h1>
 </center>
 <hr />
 {descp}
 <hr />
</body>
</html>
        """.format(namer=name,descp=desc))
    print("Html file generated")

except:
    print("Error when opening file!")