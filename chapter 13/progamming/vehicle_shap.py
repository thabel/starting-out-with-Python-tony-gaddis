# This program draws a rectangle on a Canvas.
import tkinter


class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the Canvas widget.
        self.canvas = tkinter.Canvas(self.main_window, width=450, height=450)

        # Draw a rectangle.
        A = 80,140
        self.canvas.create_text(A,text='A')
        B = 270,140
        # self.canvas.create_text(B,text='B')
        C = 270,35
        self.canvas.create_text(C,text='C')
        D = 320,35
        self.canvas.create_text(D,text='D')
        E = 420,140
        self.canvas.create_text(E,text='E')
        F = 420,180
        self.canvas.create_text(F,text='F')
        G = 320,180
        self.canvas.create_text(G,text='G')
        self.canvas.create_line(A,B,C,D,E,F,G)
        # drawing 1 
        H = 270,180
        self.canvas.create_text(H,text='H')
        I = 180,180
        self.canvas.create_text(I,text='I')
        self.canvas.create_line(H,I)
        # drawing 2
        J = 140,180
        self.canvas.create_text(J,text='J')
        K = 80,180
        self.canvas.create_text(K,text='K')
        self.canvas.create_line(J,K)
        # drawing 3
        L = 280,140
        self.canvas.create_text(L,text='L')
        M = 280,45
        self.canvas.create_text(M,text='M')
        N = 320,45
        self.canvas.create_text(N,text='N')
        O = 370,100
        self.canvas.create_text(O,text='O')
        P = 370,140
        wheel1 = J[0],J[1]-30 ,I[0],I[1]+30  
        wheel2 = H[0],H[1]-30 ,G[0],G[1]+30  
        self.canvas.create_text(P,text='P')
        self.canvas.create_line(L,M,N,O,P,L)
        self.canvas.create_line(K,A)
        self.canvas.create_oval(wheel1)
        self.canvas.create_oval(wheel2)
        # Pack the canvas.
        self.canvas.pack()
        

        # Start the mainloop.
        tkinter.mainloop()

        # Create an instance of the MyGUI class.


my_gui = MyGUI()
