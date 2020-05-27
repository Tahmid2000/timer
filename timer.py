from tkinter import *
import time


class App():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('450x250')
        self.root.title("Timer/Stopwatch")
        self.isOn = False
        self.root.resizable(width=False, height=False)
        self.label = Label(text="")
        self.button1 = Button(text="")
        self.button1.pack()
        self.button2 = Button(text="")
        self.button2.pack()
        self.buttons()
        self.initial()
        self.root.mainloop()

    def initial(self):
        self.label.configure(text='{:02d}:{:02d}:{:02d}'.format(
            0, 0, 0), font=("Arial Regular", 90))
        self.label.pack()
        self.label.place(relx=.5, rely=.3, anchor="center")
        self.button1.configure(text="START")

    def stopwatch(self):
        end = time.time()
        temp = int(end-self.now)
        hours = temp//3600
        temp = temp - 3600*hours
        minutes = temp//60
        seconds = temp - 60*minutes
        final = ('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
        self.label.configure(text=final)
        self.root.after(1000, self.stopwatch)

    def timerCall(self):
        self.button1.configure(text="PAUSE", command=self.initial)
        self.end = time.time() + 15 + 1
        self.timer()

    def timer(self):
        temp = int(self.end-time.time())
        hours = temp//3600
        newtemp = temp - 3600*hours
        minutes = newtemp//60
        seconds = newtemp - 60*minutes
        final = ('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
        self.label.configure(text=final)
        if self.button1['text'] == 'PAUSE' and temp > -1:
            self.root.after(1000, self.timer)
        else:
            temp = self.end
            self.initial()
            self.button1.configure(text="START", command=self.timerCall)

    def buttons(self):
        b1 = self.button1
        b1.configure(text="START", width=10, height=2, highlightbackground='Red',
                     fg="Black", highlightthickness=1, font=("Arial Regular", 15))
        b1.place(relx=.3, rely=.70, anchor="center")
        b2 = self.button2
        b2.configure(text="RESET", width=10, height=2, highlightbackground='Blue',
                     fg="Black", highlightthickness=1, font=("Arial Regular", 15))
        b2.place(relx=.7, rely=.70, anchor="center")
        self.button1.configure(command=self.timerCall)
        self.button2.configure(command=self.timerCall)


# fix start and stop
app = App()
