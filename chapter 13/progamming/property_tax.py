# 3
import tkinter


class MyGui:
    def __init__(self):
        self.mainwindow = tkinter.Tk()
        self.var = tkinter.StringVar()
        

        # Frame 1
        self.frame1 = tkinter.Frame(self.mainwindow)
        self.label1 = tkinter.Label(
            self.frame1, text="Enter the value of property: "
        )
        self.entry1 = tkinter.Entry(self.frame1)

       
        # Outs
        self.frame3 =  tkinter.Frame(self.mainwindow)
        self.out = tkinter.Label(self.frame3, textvariable=self.var)
        self.btn1 = tkinter.Button(
            self.frame3, text="Calculate tax", command=self.calculate
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
        out = float(self.entry1.get())
        out = out*0.6
        tax = out*0.075
        out = str(round(out,2))
        tax = str(round(tax,2))
        self.var.set("Assessment value is $"+out+"\nTax value is $"+tax)
     


MyGui()
