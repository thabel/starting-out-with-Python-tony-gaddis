# This program draws a rectangle on a Canvas.
import tkinter


class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the Canvas widget.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Draw a rectangle.
        cordinate = 20, 20, 180, 180
        self.canvas.create_rectangle(cordinate,dash=(5,2),width=3)

        # Pack the canvas.
        self.canvas.pack()

        # Start the mainloop.
        tkinter.mainloop()

        # Create an instance of the MyGUI class.


my_gui = MyGUI()
