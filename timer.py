from tkinter import *
import time
import math
import os


class Timer():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('475x275')
        self.root.title("Timer/Stopwatch")
        self.newtext = ""
        self.root.resizable(width=False, height=False)
        self.label = Label(text="")
        self.entry_text = StringVar()
        self.entry = Entry(textvariable=self.entry_text)
        self.entry.insert(0, "")
        self.button1 = Button(text="")
        self.button2 = Button(text="")
        self.button3 = Button(text="")
        self.button4 = Button(text="")
        self.state_buttons()
        self.tab_buttons()
        self.initial()
        self.root.mainloop()

    def calculate_final(self, n):
        final = ""
        hours = n//3600
        newtemp = n - 3600*hours
        minutes = newtemp//60
        seconds = newtemp - 60*minutes
        if hours == 0 and minutes != 0:
            final = ('{:01d}:{:02d}'.format(minutes, seconds))
        elif hours == 0 and minutes == 0:
            final = (':{:02d}'.format(seconds))
        else:
            final = ('{:01d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
        return final

    def character_limit(self, entry_text):
        onlynums = entry_text.get().replace(':', "")
        num_filter = filter(str.isdigit, onlynums)
        onlynums = "".join(num_filter)[0:6]
        if onlynums.startswith('0'):
            onlynums = onlynums[1:]
        self.entry.delete(0, END)
        if len(onlynums) == 1:
            self.entry.insert(0, onlynums)
        if len(onlynums) == 2:
            self.entry.insert(0, ":" + onlynums)
        if len(onlynums) == 3:
            self.entry.insert(0, onlynums[0] + ":" + onlynums[1:3])
        if len(onlynums) == 4:
            self.entry.insert(0, onlynums[0:2] + ":" + onlynums[2:4])
        if len(onlynums) == 5:
            self.entry.insert(0, onlynums[0] + ":" +
                              onlynums[1:3] + ":" + onlynums[3:5])
        if len(onlynums) >= 6:
            self.entry.insert(0, onlynums[0:2] + ":" +
                              onlynums[2:4] + ":" + onlynums[4:6])
        self.entry.icursor("end")

    def initial(self):
        self.entry.configure(justify="right", font=(
            "Arial Regular", 90), width=7)
        self.label.configure(text="00:00:00", font=("Arial Regular", 90))
        self.label.place(relx=.5, rely=.35, anchor="center")
        self.button1.configure(text="START", highlightbackground='green')
        self.set_timer()

    def setframeStopwatch(self):
        if self.button1['text'] == 'START':
            self.label.configure(text=':00')
            self.endtime = 0
            return
        self.label.configure(text=self.newtext)
        self.button1.configure(
            text="RESUME", command=self.stopwatchCall, highlightbackground='green')

    def stopwatchReset(self):
        self.label.configure(text=':00')
        self.endtime = 0
        self.button1.configure(
            text="START", highlightbackground='green', command=self.stopwatchCall)

    def stopwatchCall(self):
        self.button1.configure(
            text="PAUSE", command=self.setframeStopwatch, highlightbackground='red')
        self.now = time.time() - self.endtime
        self.stopwatch()

    def stopwatch(self):
        if self.button4['highlightbackground'] == 'white':
            self.newtext = ""
            return
        end = time.time()
        temp = math.floor(end-self.now)
        final = self.calculate_final(temp)
        self.newtext = final
        self.label.configure(text=final)
        if self.button1['text'] == 'PAUSE':
            self.root.after(1000, self.stopwatch)
        elif self.button1['text'] == 'START':
            self.label.configure(text=':00')
            self.endtime = 0
            return
        else:
            temp -= 1
            self.endtime = temp
            final = self.calculate_final(temp)
            self.label.configure(text=final)
            if self.endtime == 0:
                self.label.configure(text=':00')
                self.endtime = 0
                self.button1.configure(
                    text="START", command=self.stopwatchCall, highlightbackground='green')
                return

    def setframeTimer(self):
        if self.button1['text'] == 'START':
            self.endtime = 1800
            return
        self.label.configure(text=self.newtext)
        self.button1.configure(
            text="RESUME", command=self.timerCall, highlightbackground='green')

    def timerReset(self):
        self.entry.place_forget()
        self.label.place(relx=.5, rely=.35, anchor="center")
        self.button1.configure(
            text="START", highlightbackground='green', command=self.timerCall)
        temp = self.endtime
        self.reset = self.calculate_final(temp)
        self.label.configure(text=self.calculate_final(self.init))

    def timerCall(self):
        if self.button1['text'] != 'RESUME':
            self.entry.place_forget()
            self.label.place(relx=.5, rely=.35, anchor="center")
            self.new_value()
        self.end = time.time() + self.endtime + 1
        self.button2.configure(state='normal')
        self.button1.configure(
            text="PAUSE", command=self.setframeTimer, highlightbackground='red')
        self.timer()

    def timer(self):
        if self.button3['highlightbackground'] == 'white':
            return
        temp = math.floor(self.end-time.time())
        final = self.calculate_final(temp)
        self.label.configure(text=final)
        self.newtext = final
        if self.button1['text'] == 'PAUSE' and temp > 0:
            self.root.after(1000, self.timer)
        elif temp == 0:
            self.endtime = 1800
            self.button1.configure(
                text="START", command=self.timerCall, highlightbackground='green')
            os.system("afplay tink2.wav&")
            os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format("Time Up!", "Timer"))
        elif self.button1['text'] == 'START':
            self.label.configure(text=self.reset)
            return
        else:
            temp += 1
            self.endtime = temp
            final = self.calculate_final(temp)
            self.label.configure(text=final)

    def state_buttons(self):
        self.button1.configure(text="START", width=10, height=2, highlightbackground='green',
                               fg="Black", font=("Arial Regular", 15), cursor="pointinghand")
        self.button1.place(relx=.3, rely=.70, anchor="center")
        self.button2.configure(text="RESET", width=10, height=2, fg="Black", font=(
            "Arial Regular", 15), cursor="pointinghand")
        self.button2.place(relx=.7, rely=.70, anchor="center")

    def tab_buttons(self):
        self.button3.configure(text="Timer", width=10, height=1, highlightthickness=1,
                               font=("Arial Regular", 12), command=self.set_timer, cursor="pointinghand")
        self.button3.place(relx=.41, rely=.1, anchor="center")
        self.button4.configure(text="Stopwatch", width=10, height=1, highlightthickness=1,
                               font=("Arial Regular", 12), command=self.set_stop, cursor="pointinghand")
        self.button4.place(relx=.59, rely=.1, anchor="center")

    def click(self, event):
        self.paused = False
        self.timerReset()
        self.label.place_forget()
        self.entry.place(relx=.5, rely=.35, anchor="center")
        self.entry.delete(0, END)
        self.entry.insert(0, "")
        self.button2.configure(state='disabled')
        self.entry.focus_set()
        self.entry.icursor("end")
        self.entry_text.trace(
            "w", lambda *args: self.character_limit(self.entry_text))

    def click2(self, event):
        self.button2.configure(state='normal')
        self.label.place(relx=.5, rely=.35, anchor="center")
        self.entry.place_forget()
        self.new_value()

    def new_value(self):
        if self.button1['text'] != 'RESUME':
            values = self.entry_text.get().split(':')
            values = [s for s in values if s.isdigit()]
            if len(values) != 0:
                values = list(map(int, values))
                if len(values) == 1:
                    self.endtime = values[0]
                    self.label.configure(text=':{:02d}'.format(values[0]))
                if len(values) == 2:
                    self.endtime = values[0]*60 + values[1]
                    self.label.configure(
                        text='{:01d}:{:02d}'.format(values[0], values[1]))
                if len(values) == 3:
                    self.endtime = values[0] * 3600 + values[1]*60 + values[2]
                    self.label.configure(text='{:01d}:{:02d}:{:02d}'.format(
                        values[0], values[1], values[2]))
            self.init = self.endtime
        else:
            pass

    def enter(self, event):
        self.button2.configure(state='normal')
        self.click2(event)
        self.entry.place_forget()
        self.label.place(relx=.5, rely=.35, anchor="center")
        self.timerCall()

    def set_timer(self):
        self.newtext = ""
        self.endtime = 1800
        self.init = 1800
        self.entry.delete(0, 'end')
        self.entry.insert(0, "")
        self.label.bind(
            "<Button-1>", self.click)
        self.entry.bind("<Button-1>", self.click2)
        self.timerReset()
        self.entry.bind("<Return>", self.enter)
        self.button2.configure(state='normal')
        self.button1.configure(command=self.timerCall)
        self.button2.configure(command=self.timerReset)
        self.button3.configure(state="disabled")
        self.button4.configure(state="normal")
        self.button3.configure(highlightbackground="blue")
        self.button4.configure(highlightbackground="white")

    def set_stop(self):
        self.entry.unbind("<Button-1>")
        self.entry.unbind("<Return>")
        self.label.unbind("<Button-1>")
        self.entry.insert(0, "")
        self.entry.place_forget()
        self.label.place(relx=.5, rely=.35, anchor="center")
        self.endtime = 0
        self.stopwatchReset()
        self.button1.configure(command=self.stopwatchCall)
        self.button2.configure(command=self.stopwatchReset)
        self.button4.configure(state="disabled")
        self.button3.configure(state="normal")
        self.button4.configure(highlightbackground="blue")
        self.button3.configure(highlightbackground="white")


# design(ttk)
if __name__ == '__main__':
    app = Timer()
