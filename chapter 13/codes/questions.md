1. What is a user interface?
User interface is the part of the computer with which the user interacts.
2. How does a command line interface work?
A command line interface typically displays a prompt, and the user 
types a command, which is then executed.
3. When the user runs a program in a text-based environment, such as the command 
line, what determines the order in which things happen?
the program
4. What is an event-driven program
programs that respond to the actions of the user

5. Briefly describe each of the following tkinter widgets:
a) Label 
An area that displays one line of text or an image
b) Entry
An area in which the user may type a single line of input from the keyboard
c) Button
A button that can cause an action to occur when it is clicked.
d) Frame
A container that can hold other widgets.

6. How do you create a root widget?
tkinter.Tk()

7. What does the tkinter module’s mainloop function do?
This function runs like an infinite loop until you close the main window.

8. What does a widget’s pack method do?

The pack method determines where a widget should be positioned and makes the widget visible when the main window is displayed. (You call the pack method for each widget in a window.)

9. If you create two Label widgets and call their pack methods with no arguments, 
how will the Label widgets be arranged inside their parent widget?

two Label widgets are displayed with one stacked on top of the other

10. What argument would you pass to a widget’s pack method to specify that it 
should be positioned as far left as possible inside the parent widget?

side='left'

11. How do you retrieve data from an Entry widget?

the get method

12. When you retrieve a value from an Entry widget, of what data type is it?

string

13. What module is the StringVar class in?

tkinter

14. What can you accomplish by associating a StringVar object with a Label widget?

modifing the value of a label 

13.15 You want the user to be able to select only one item from a group of items. 
Which type of component would you use for the items, radio buttons or check 
buttons?

Radio
13.16 You want the user to be able to select any number of items from a group of 
items. Which type of component would you use for the items, radio buttons or 
check buttons?

check

17. How can you use an IntVar object to determine which Radiobutton has been 
selected in a group of Radiobuttons?

Create one IntVar , the value of intvar is assigned to the the selected
radio button

18. How can you use an IntVar object to determine whether a Checkbutton has 
been selected?

Create  mutiple intvar , selected check button will have this intvar
set to 1.


19. In the Canvas widget’s screen coordinate system, what are the coordinates of the 
pixel in the upper-left corner of the window?

0,0

20. Using the Canvas widget’s screen coordinate system with a window that is 
640 pixels wide by 480 pixels high, what are the coordinates of the pixel in 
the lower-right corner?

139,479

21. How is the Canvas widget’s screen coordinate system different from the 
Cartesian coordinate system used by the turtle graphics library?

When you scroll donw the y coordinate increases in the canvas 
but decreases in the turtle


22. What Canvas widget methods would you use to draw each of the following types 
of shapes?
a) A circle # create_oval()
b) A square # create_rectangle()
c) A rectangle # create_reactangle
d) A closed six-sided shape # create_polygon()
e) An ellipse # create_oval()
f) An arc # create_arc


