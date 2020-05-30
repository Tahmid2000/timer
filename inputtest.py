from tkinter import *
import time
import math


class Timer():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('475x275')
        self.root.title("Timer/Stopwatch")
        self.newtext = ""
        self.root.resizable(width=False, height=False)
        self.entry_text = StringVar()
        self.label = Entry(text="", justify="right",
                           textvariable=self.entry_text)
        self.label.insert(0, "")
        self.button1 = Button(text="")
        self.button2 = Button(text="")
        self.button3 = Button(text="")
        self.button4 = Button(text="")
        self.state_buttons()
        self.tab_buttons()
        self.initial()
        self.root.mainloop()

    def character_limit(self, entry_text):
        onlynums = entry_text.get().replace(':', "")
        self.label.delete(0, END)
        if len(onlynums) == 1:
            self.label.insert(0, onlynums)
        if len(onlynums) == 2:
            self.label.insert(0, ":" + onlynums)
        if len(onlynums) == 3:
            self.label.insert(0, onlynums[0] + ":" + onlynums[1:3])
        if len(onlynums) == 4:
            self.label.insert(0, onlynums[0:2] + ":" + onlynums[2:4])
        if len(onlynums) == 5:
            self.label.insert(0, onlynums[0] + ":" +
                              onlynums[1:3] + ":" + onlynums[3:5])
        if len(onlynums) >= 6:
            self.label.insert(0, onlynums[0:2] + ":" +
                              onlynums[2:4] + ":" + onlynums[4:6])
        self.label.icursor("end")

    def initial(self):
        self.label.configure(font=("Arial Regular", 90), width=7)
        self.label.icursor(0)
        self.entry_text.trace(
            "w", lambda *args: self.character_limit(self.entry_text))
        self.label.pack()
        self.label.place(relx=.5, rely=.35, anchor="center")
        self.button1.configure(text="START", highlightbackground='green')
        # self.set_timer()

    def tab_buttons(self):
        self.button3.pack()
        self.button4.pack()
        self.button3.configure(text="Timer", width=10, height=1, highlightthickness=1,
                               font=("Arial Regular", 12), cursor="pointinghand")
        self.button3.place(relx=.41, rely=.1, anchor="center")
        self.button4.configure(text="Stopwatch", width=10, height=1, highlightthickness=1,
                               font=("Arial Regular", 12), cursor="pointinghand")
        self.button4.place(relx=.59, rely=.1, anchor="center")

    def state_buttons(self):
        self.button1.pack()
        self.button2.pack()
        self.button1.configure(text="START", width=10, height=2, highlightbackground='green',
                               fg="Black", font=("Arial Regular", 15), cursor="pointinghand")
        self.button1.place(relx=.3, rely=.70, anchor="center")
        self.button2.configure(text="RESET", width=10, height=2, highlightbackground='Blue',
                               fg="Black", font=("Arial Regular", 15), cursor="pointinghand")
        self.button2.place(relx=.7, rely=.70, anchor="center")


app = Timer()
