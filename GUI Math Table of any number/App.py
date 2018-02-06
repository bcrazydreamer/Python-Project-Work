try:
    from tkinter import *
except:
    from Tkinter import *
import os
import io
from tkinter import font
from tkinter import messagebox

table=Tk()
table.geometry("420x610+500+50")
table.resizable(width=False, height=False)
f=font.Font(family='Helvetica', size=20, weight='bold')
color="#76FF03" #All place color
try:
    table.iconbitmap(r'icon/icon.ico')
except:
    pass

table.title("Math Tables")
table.configure(background=color)

#frame creates a saparater line
frame = Frame(table, bg='green',background="black")
frame.pack(fill='x')

#Starting Text
head=Label(text="Which Table You Want",height="1",width="35",font=("Arial", 16),background="#FFFF00")
head.pack()
frame = Frame(table, bg='green',background="black")
frame.pack(fill='x')

def result():
    a=inputbox.get()      
    try:
        a=int(a)
        pos=200
        xpos=145
        result.listbox = Listbox(table,justify='center',width=25, height=12,font=f,background="#000",fg="white")# Initialize List Box
        result.listbox.place(x=19,y=200)
        for i in range(1,11):
            
            ans=a*i
            i=str(i)
            string=str(a)+"x"+i+"="+str(ans)
            result.listbox.insert(END, string)
            pos=pos+40
            
            
    except:
        try:
            a=float(a)
            pos=200
            xpos=145
            result.listbox = Listbox(table,justify='center',width=25, height=12,font=f,background="#000",fg="white")# Initialize List Box
            result.listbox.place(x=19,y=200)
            for i in range(1,11):
                
                ans=a*i
                i=str(i)
                string=str(a)+"x"+i+"="+str(ans)
                result.listbox.insert(END, string)
                pos=pos+40
        except:
            if a=="":
                msg=messagebox.showinfo( "Error", "Please Enter Value")
            else:    
                msg=messagebox.showinfo( "Error", "Please Enter Positive Numeric Value")
            
def clear():
        #Initialize List Box
        result.listbox = Listbox(table,width=25, height=12,font=f,background="#000",fg="white")
        result.listbox.place(x=19,y=200)

#image
photo = PhotoImage(file="pic/logo.gif")
w = Label(table, image=photo,background=color,bd=1)
w.photo = photo
w.pack()
frame = Frame(table, bg='green',background="black")
frame.pack(fill='x')

inputbox=Entry(width=50)
inputbox.pack()
    
photo1 = PhotoImage(file="button/submit.gif")
b=Button(table,image=photo1,command=result)
b.photo1 = photo1
b.place(x=120,y=155)
photo2 = PhotoImage(file="button/clear.gif")
b=Button(table,image=photo2,command=clear)
b.photo2 = photo2
b.place(x=260,y=155)
mainloop()
