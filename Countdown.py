from tkinter import *

root = Tk()

hour_fetch = StringVar(value="0")
minute_fetch = StringVar(value="0")
second_fetch = StringVar(value="0")

time_in_seconds = 0

def Start_countdowns():
    global time_in_seconds
    try:
        h = int(hour_fetch.get())
        m = int(minute_fetch.get())
        s = int(second_fetch.get())
    except ValueError:
        return 
    time_in_seconds = h * 3600 + m * 60 + s
    countdown()

def countdown():
    global time_in_seconds

    if time_in_seconds <= 0:
        Label(text="Your time is up").grid(row=3, column=2)
        return

    hrs, rem = divmod(time_in_seconds, 3600)
    mins, secs = divmod(rem, 60)

    hour_fetch.set(str(hrs))
    minute_fetch.set(str(mins))
    second_fetch.set(str(secs))

    time_in_seconds -= 1
    root.after(1000, countdown)  # run again in 1 second

Hour = Entry(root, textvariable=hour_fetch, width=5)
Minute = Entry(root, textvariable=minute_fetch, width=5)
Second = Entry(root, textvariable=second_fetch, width=5)

Start_countdown = Button(root, text="Start Countdown", command=Start_countdowns)

Hour.grid(row=1, column=1)
Minute.grid(row=1, column=2)
Second.grid(row=1, column=3)
Start_countdown.grid(row=2, column=2)

root.mainloop()
