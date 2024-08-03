1 # This program draws text on a Canvas.
 2 import tkinter
 3 import tkinter.font
 4
 5 class MyGUI:
 6 def __init__(self):
 7 # Create the main window.
 8 self.main_window = tkinter.Tk()
 9
10 # Create the Canvas widget.
11 self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
12
13 # Create a Font object.
14 myfont = tkinter.font.Font(family='Helvetica', size=18, weight='bold')
15 
16 # Display some text.
17 self.canvas.create_text(100, 100, text='Hello World', font=myfont)
18 
19 # Pack the canvas.
20 self.canvas.pack()
21 
22 # Start the mainloop.
23 tkinter.mainloop()
24
25 # Create an instance of the MyGUI class.
26 my_gui = MyGUI()