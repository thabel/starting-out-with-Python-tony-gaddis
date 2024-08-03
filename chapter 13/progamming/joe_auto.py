# This program demonstrates a group of Checkbutton widgets.
import tkinter
import tkinter.messagebox

data = (
            ("Oil change", 30.00),
            ("Lube job", 20.00),
            ("Radiator flush", 40.00),
            ("Transmission flush", 100.00),
            ("Inspection", 35.00),
            ("Muffler replacement", 200.00),
            ("Tire rotation", 20.00),
        )

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        
        print(data)
        # Create two frames. One for the checkbuttons
        # and another for the regular Button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create three IntVar objects to use with
        # the Checkbuttons.
        self.vars = [
            tkinter.IntVar()
             for i in range(len(data))
        ]
        self.cboxes = [
            tkinter.Checkbutton(
            self.top_frame, text=data[i][0]+" "+str(data[i][1])+"$", variable=self.vars[i])
            for i in range(len(data))

        ]
        for i  in range(len(data)):
            self.vars[i].set(0)
            self.cboxes[i].pack()
       
        
        # Create an OK button and a Quit button.
        self.ok_button = tkinter.Button(
            self.bottom_frame, text="OK", command=self.show_choice
        )
        self.var = tkinter.StringVar()
        self.out = tkinter.Label(self.bottom_frame, textvariable=self.var)

        
        # Pack the Buttons.
        self.ok_button.pack()
        self.out.pack()

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start the mainloop.
        tkinter.mainloop()

        # The show_choice method is the callback function for the
        # OK button.

    def show_choice(self):
        total = 0
        for i in range(len(data)):
            if self.vars[i].get() == 1:
                total += data[i][1]
        self.var.set("Total is "+str(round(total,2)))


    # Create an instance of the MyGUI class.


my_gui = MyGUI()
