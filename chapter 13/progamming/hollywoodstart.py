# This program draws a rectangle on a Canvas.
import tkinter


class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the Canvas widget.
        self.canvas = tkinter.Canvas(self.main_window, width=400, height=400)

        # Draw a rectangle.
        A = 70,150
        # self.canvas.create_text(A,text='A')
        B = 150,150
        # self.canvas.create_text(B,text='B')
        C = 180,70
        # self.canvas.create_text(C,text='C')
        D = 210,150
        # self.canvas.create_text(D,text='D')
        E = 290,150
        # self.canvas.create_text(E,text='E')
        F = 210,210
        # self.canvas.create_text(F,text='F')
        G = 290,300
        # self.canvas.create_text(G,text='G')
        H = 180,240
        # self.canvas.create_text(H,text='H')
        I = 70,300
        # self.canvas.create_text(I,text='I')
        J = 150,210
        # self.canvas.create_text(J,text='J')
        self.canvas.create_line(A,B,C,D,E,F,G,H,I,J,A)

        # Pack the canvas.
        self.canvas.pack()

        # Start the mainloop.
        tkinter.mainloop()

        # Create an instance of the MyGUI class.


my_gui = MyGUI()
