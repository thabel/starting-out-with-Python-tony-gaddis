# This program demonstrates a group of Checkbutton widgets.
import tkinter
import tkinter.messagebox

data = (
    ("Daytime (6:00 a.m. through 5:59 p.m.)", 0.07),
    ("Evening (6:00 p.m. through 11:59 p.m.)", 0.12),
    ("Off-Peak (midnight through 5:59 a.m.)", 0.05),
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
        self.label1 = tkinter.Label(self.top_frame, text="Select Rate category")
        self.label1.pack()

        # Create three IntVar objects to use with
        self.radio_var = tkinter.IntVar()

        # Set the intVar object to 1.
        self.radio_var.set(0)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(
            self.top_frame,
            text=data[0][0] + " " + str(data[0][1]) + "$",
            variable=self.radio_var,
            value=0,
        )
        self.rb2 = tkinter.Radiobutton(
            self.top_frame,
            text=data[1][0] + " " + str(data[1][1]) + "$",
            variable=self.radio_var,
            value=1,
        )
        self.rb3 = tkinter.Radiobutton(
            self.top_frame,
            text=data[2][0] + " " + str(data[2][1]) + "$",
            variable=self.radio_var,
            value=2,
        )

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Create an OK button and a Quit button.
        self.frame3 = tkinter.Frame(self.main_window)
        self.entry1 = tkinter.Entry(self.frame3)
        self.label2 = tkinter.Label(self.frame3, text="Enter the number of minutes: ")
        self.label2.pack(side="left")
        self.entry1.pack(side="left")

        self.ok_button = tkinter.Button(
            self.bottom_frame, text="OK", command=self.show_choice
        )

        self.var = tkinter.StringVar()
        self.out = tkinter.Label(self.bottom_frame, textvariable=self.var)

        # Pack the frames.
        self.top_frame.pack()

        self.frame3.pack()
        self.bottom_frame.pack()

        # Pack the Buttons.
        self.ok_button.pack()
        self.out.pack()

        # Start the mainloop.
        tkinter.mainloop()

        # The show_choice method is the callback function for the
        # OK button.

    def show_choice(self):
        total = 0
        i = self.radio_var.get()
        num = int(self.entry1.get())
        total = num * data[i][1]
        self.var.set("Total is $" + str(round(total, 2)))

    # Create an instance of the MyGUI class.


my_gui = MyGUI()
