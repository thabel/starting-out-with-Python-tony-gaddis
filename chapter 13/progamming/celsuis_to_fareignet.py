# 3
import tkinter


class MyGui:
    def __init__(self):
        self.mainwindow = tkinter.Tk()
        self.var = tkinter.StringVar()

        

        # Frame 1
        self.frame1 = tkinter.Frame(self.mainwindow)
        self.label1 = tkinter.Label(
            self.frame1, text="Enter the celsius Temperature: "
        )
        self.entry1 = tkinter.Entry(self.frame1)

        

        # Outs
        self.frame3 =  tkinter.Frame(self.mainwindow)
        self.out = tkinter.Label(self.frame3, textvariable=self.var)
        self.btn1 = tkinter.Button(
            self.frame3, text="Convert to Fahrenhiet", command=self.calculate
        )
        # Packs
        self.label1.pack(side="left")
        self.entry1.pack(side="left")
        self.frame1.pack()


        self.frame3.pack()
        self.out.pack()
    

        self.btn1.pack()

        tkinter.mainloop()

    def calculate(self):
        temp = float(self.entry1.get())*9/5+32
        temp = str(round(temp,2))
        self.var.set("F :"+temp)
        print("F",temp)


MyGui()
