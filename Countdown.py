from tkinter import *
import time

root = Tk()




hour_fetch = (StringVar())
minute_fetch = (StringVar())
second_fetch = (StringVar())

def Start_countdowns():
    Minute_in_seconds = int(minute_fetch.get()) * 60
    Hour_in_seconds = int(hour_fetch.get()) * 3600
    time_in_seconds = int(second_fetch.get()) + Hour_in_seconds + Minute_in_seconds
    time_in_seconds -= 1
    print(time_in_seconds)
    if time_in_seconds == 0:
        print("time's up")
    while time_in_seconds >= 0:
        mins, secs = divmod(time_in_seconds, 60)
        hrs, mins = divmod(mins,60)
        

Start_countdown = Button(root,text="Start Countdown",command=Start_countdowns)

Hour = Entry(root,textvariable=hour_fetch)
Minute = Entry(root,textvariable=minute_fetch)
Second = Entry(root,textvariable=second_fetch)

Hour.grid(row=1,column=1)
Minute.grid(row=1,column=2)
Second.grid(row=1,column=3)
Start_countdown.grid(row=2,column=2)
root.mainloop()