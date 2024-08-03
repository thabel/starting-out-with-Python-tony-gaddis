# 3
import tkinter


class MyGui:
    def __init__(self):
        self.mainwindow = tkinter.Tk()
        self.var = tkinter.StringVar()

        

        # Frame 1
        self.frame1 = tkinter.Frame(self.mainwindow)
        self.label1 = tkinter.Label(
            self.frame1, text="Enter the number of gallons: "
        )
        self.entry1 = tkinter.Entry(self.frame1)

        # Frame 2
        self.frame2 = tkinter.Frame(self.mainwindow)
        self.label2 = tkinter.Label(
            self.frame2,
            text="Enter number of miles it can be driven on a full tank: ",
        )
        self.entry2 = tkinter.Entry(self.frame2)

        # Outs
        self.frame3 =  tkinter.Frame(self.mainwindow)
        self.out = tkinter.Label(self.frame3, textvariable=self.var)
        self.btn1 = tkinter.Button(
            self.frame3, text="Calculate MPG", command=self.calculate
        )
        # Packs
        self.label1.pack(side="left")
        self.entry1.pack(side="left")
        self.frame1.pack()

        self.label2.pack(side="left")
        self.entry2.pack(side="left")
        self.frame2.pack()

        self.frame3.pack()
        self.out.pack()
    

        self.btn1.pack()

        tkinter.mainloop()

    def calculate(self):
        mpg = float(self.entry1.get())/float(self.entry2.get())
        mpg = str(round(mpg,2))
        self.var.set("Mpg :"+mpg)
        print("mpg",mpg)


MyGui()
