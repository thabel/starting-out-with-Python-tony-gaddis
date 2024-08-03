# 1
import tkinter


class MyGui:
    latin_english_words = {
        "sinister": "left",
        "medium": "center",
        "dexter": "right",
    }

    def __init__(self):
        self.mainwindow = tkinter.Tk()
        self.var = tkinter.StringVar()

        self.btn1 = tkinter.Button(
            self.mainwindow, text="QUIT", command=self.mainwindow.destroy
        )
        self.btns = []
        for key in self.latin_english_words:
            print("key", key)
            self.btns.append(
                tkinter.Button(self.mainwindow, text=key, command=self.f_wrapper(key))
            )

        self.out = tkinter.Label(self.mainwindow, textvariable=self.var)

        for btn in self.btns:
            btn.pack(side="left", pady=50, padx=10)

        self.out.pack(side="bottom")
        self.btn1.pack(side="bottom")
        tkinter.mainloop()

    def f_wrapper(self, text):
        def display_translation():
            print("called with text", text)
            self.var.set("Translation :" + self.latin_english_words[text])

        return display_translation


MyGui()
