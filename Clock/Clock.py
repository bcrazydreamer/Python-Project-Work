from tkinter import *
import time
from datetime import date
import calendar
root=Tk()
root.geometry("600x600+382+92")
root.title("Clock")

def clock():
    clk=Tk()
    clk.geometry("500x300+382+92")
    clk.resizable(height=False,width=False)
    clock.x=time.ctime()
    clock.h=((clock.x[11])+(clock.x[12]))
    if(int(clock.h)>12):
        if(int(clock.h)>12):
            clock.status="PM"
        else:
            clock.status="AM"
        clock.h=str(int(clock.h)-12)
    #-----------------------------------------------
    clock.m=(clock.x[14])+(clock.x[15])
    clock.s=(clock.x[17])+(clock.x[18])
    clock.tym=clock.h+":"+clock.m+":"+clock.s 
    lbl=Label(clk,text=clock.tym,font=('',65),bd=5) #Time
    lbl.place(x=85,y=55)
    #-------------------------------------------------
    lbl=Label(clk,text=clock.status,font=('',40),bd=5) #AM PM
    lbl.place(x=210,y=5)
    #-------------------------------------------------
    lbl=Label(clk,text=daydate.day,font=('',25)) #Day
    lbl.place(x=170,y=140)
    #-------------------------------------------------
    lbl=Label(clk,text=daydate.date,font=('',35)) #Date
    lbl.place(x=85,y=200)
def daydate():
    daydate.mydate = date.today()
    daydate.day=calendar.day_name[daydate.mydate.weekday()]
    y=daydate.mydate.year
    dat=daydate.mydate.day
    mon=daydate.mydate.month
    if mon==1:
        mon="January"
    elif mon==2:
        mon="February"
    elif mon==3:
        mon="March"
    elif mon==4:
        mon="April"
    elif mon==5:
        mon="May"
    elif mon==6:
        mon="June"
    elif mon==7:
        mon="July"
    elif mon==8:
        mon="August"
    elif mon==9:
        mon="September"
    elif mon==10:
        mon="October"
    elif mon==11:
        mon="November"
    else:
        mon="December"
    daydate.date=str(dat)+" "+str(mon)+" "+str(y)    
daydate()
clock()
root.destroy()
root.mainloop()
#datetime.datetime.today().weekday()
