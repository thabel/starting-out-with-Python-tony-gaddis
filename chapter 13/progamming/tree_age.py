# This program draws two ovals on a Canvas.
import tkinter


class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the Canvas widget.
        self.canvas = tkinter.Canvas(self.main_window, width=400, height=400)

        # Draw two ovals.
        offset = 0
        for i in range(5):
            self.canvas.create_oval(150 -offset, 150-offset, 250+offset, 250+offset)
            
            offset += 30
        text_offset = 60
        self.canvas.create_text(200, 200, text="1st ring")
        self.canvas.create_text(200, 200-text_offset, text="2nd ring")
        text_offset += 30
        self.canvas.create_text(200, 200-text_offset, text="3td ring")
        text_offset += 30
        self.canvas.create_text(200, 200-text_offset, text="4th ring")
        text_offset += 30
        self.canvas.create_text(200, 200-text_offset, text="5th ring")
      
        # self.canvas.create_oval(150 -offset, 150-offset, 250+offset, 250+offset)

        # self.canvas.create_oval(150 -offset, 150-offset, 250+offset, 250+offset)

        # self.canvas.create_oval(150 -offset, 150-offset, 250+offset, 250+offset)

        # self.canvas.create_oval(150 -offset, 150-offset, 250+offset, 250+offset)
        

        # Pack the canvas.
        self.canvas.pack()

        # Start the mainloop.
        tkinter.mainloop()

    # Create an instance of the MyGUI class.


my_gui = MyGUI()
