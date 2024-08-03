# This program draws a rectangle on a Canvas.
import tkinter


class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the Canvas widget.
        self.canvas = tkinter.Canvas(self.main_window, width=400, height=400)

        # Draw a rectangle.
        cordinate = 140, 170, 280, 280
        self.canvas.create_rectangle(cordinate)
        door_rec = (140+280)/2-15,280-40,(140+280)/2+15,280
        win1 =  150,200,170,220
        win2 =  150+100,200,170+100,220
        self.canvas.create_line(140, 170,(140+280)/2,100, 280, 170)
        self.canvas.create_rectangle(door_rec)
        self.canvas.create_rectangle(win1)
        self.canvas.create_rectangle(win2)
        # Pack the canvas.
        self.canvas.pack()

        # Start the mainloop.
        tkinter.mainloop()

        # Create an instance of the MyGUI class.


my_gui = MyGUI()
