# 1
import tkinter
class MyGui:
    def __init__(self):
        self.mainwindow = tkinter.Tk()
        self.var = tkinter.StringVar()

        self.btn1 = tkinter.Button(self.mainwindow,text="Show info",command=self.showinfo)
        self.btn2 = tkinter.Button(self.mainwindow,text="QUIT",command=self.mainwindow.destroy)

        self.out = tkinter.Label(self.mainwindow,textvariable=self.var)
        
        self.out.pack()
        self.btn1.pack(side="left",pady=50,padx=10)
        self.btn2.pack(side="left",pady=50,padx=10)
        tkinter.mainloop()

    def showinfo(self):
        self.var.set("Steven Markus.\n274 Baily Drive\nWaynessVille,NC 27999")

    

MyGui()