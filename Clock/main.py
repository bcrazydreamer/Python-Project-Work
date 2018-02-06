from tkinter import *
import time
from datetime import date
import calendar
root=Tk()
root.geometry("500x150")
root.resizable(height=False,width=False)
root.iconbitmap("icon.ico")
root.title("Clock")
    
def clock():
    clock.x=time.ctime()
    clock.h=clock.x[11]+clock.x[12]
    clock.m=clock.x[14]+clock.x[15]
    clock.s=clock.x[17]+clock.x[18]
    clock.tym=clock.h+":"+clock.m+":"+clock.s
    clk.config(text=clock.tym)    
    clk.after(200,clock)
    
clk=Label(root,font=("","80","bold"))
clk.place(x=30,y=15)
clock()
root.mainloop()
