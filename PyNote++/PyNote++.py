try:
    from tkinter import *
except:
    from Tkinter import *
from extp import *
import os
import time
from tkinter import font
from bgclr import *
from fgclr import *
from abouttx import *
from tkinter import messagebox

root=Tk()
root.geometry("700x700+300+50")
root.iconbitmap(r'images/icon/icon.ico')
root.resizable(width=False, height=False)
root.title("Dreamer")
f=font.Font(family='Helvetica', size=15, weight='bold')
def status():
    time.sleep(1)
    status.show=Label(text="Saved Successfully",justify='center',font=font.Font(family='Helvetica', size=25, weight='bold'))
    status.show.place(x=200,y=600)
    
def text():
    text.t = Text(root, height=30, width=80,fg="blue",bd=2)
    text.t.place(x=25,y=40)
    f1=open("bgclr.py","w")
    t2="txnc=['gray95']"
    f1.write(t2)
    f1.close()
    f1=open("fgclr.py","w")
    t2="fclr=['black']"
    f1.write(t2)
    f1.close()
#--------------------------------------------------------------------
def back():
    about.new.destroy()
    try:
       text()
    except:
        return 
        
def about():
        about.new=Tk()
        about.new.geometry("700x400+300+50")
        about.new.iconbitmap(r'images/icon/icon.ico')
        about.new.configure(background="white")
        about.new.resizable(width=False, height=False)
        about.new.title("Dreamer")
        frame = Frame(about.new, bg='green',background="black")
        frame.pack(fill='x')
        btn=Button(about.new,text="Back",height="1",width="8",command=back)
        btn.place(x=310,y=5)
        about.disp=Label(about.new,text=txval,justify='center',
                         background="white",font=font.Font(family='Helvetica', size=35, weight='bold'))
        about.disp.place(x=130,y=100)
#-------------------------------------------------------------------        
        
def exit():
    root.destroy()
    
def abc():
    val=text.t.get("1.0","end-1c")
    ext=extension.get()
    nam=name.get()
    try:
        os.mkdir("files")
        file=open("files/"+nam+"."+ext,"w")
        status()
    except:
        file=open("files/"+nam+"."+ext,"w")
        status()
        
        
    file.write(val)
    file.close()
#----------Text Color--------------------------------
def txnblue():
    header = Label(text=headtext,font=f,fg="blue",background=txnc)
    header.place(x=295,y=8)
    namelbl = Label(text=fname,font=f,fg="blue",background=txnc) #fname in another file(fname-->file name)
    namelbl.place(x=295,y=530)
    f1=open("fgclr.py","w")
    t2="fclr=['blue']"
    f1.write(t2)
    f1.close()
def txngreen():
    header = Label(text=headtext,font=f,fg="green",background=txnc)
    header.place(x=295,y=8)
    namelbl = Label(text=fname,font=f,fg="green",background=txnc) #fname in another file(fname-->file name)
    namelbl.place(x=295,y=530)
    f1=open("fgclr.py","w")
    t2="fclr=['green']"
    f1.write(t2)
    f1.close()
def txnred():
    header = Label(text=headtext,font=f,fg="red",background=txnc)
    header.place(x=295,y=8)
    namelbl = Label(text=fname,font=f,fg="red",background=txnc) #fname in another file(fname-->file name)
    namelbl.place(x=295,y=530)
    f1=open("fgclr.py","w")
    t2="fclr=['red']"
    f1.write(t2)
    f1.close()
def txnyellow():
    header = Label(text=headtext,font=f,fg="yellow",background=txnc)
    header.place(x=295,y=8)
    namelbl = Label(text=fname,font=f,fg="yellow",background=txnc) #fname in another file(fname-->file name)
    namelbl.place(x=295,y=530)
    f1=open("fgclr.py","w")
    t2="fclr=['yellow']"
    f1.write(t2)
    f1.close()
def txnblack():
    header = Label(text=headtext,font=f,fg="black",background=txnc)
    header.place(x=295,y=8)
    namelbl = Label(text=fname,font=f,fg="black",background=txnc) #fname in another file(fname-->file name)
    namelbl.place(x=295,y=530)
    f1=open("fgclr.py","w")
    t2="fclr=['black']"
    f1.write(t2)
    f1.close()
#----------Background Color Blue---------------------
def blueback():
    root.configure(background=bl)
    namelbl = Label(text=fname,font=f,fg=fclr,background=bl)
    namelbl.place(x=295,y=530)
    header = Label(text=headtext,font=f,fg=fclr,background=bl)
    header.place(x=295,y=8)
    f1=open("bgclr.py","w")
    t2="txnc=['"+bl+"']"
    f1.write(t2)
    f1.close()
def default():
    root.configure(background="gray94")
    namelbl = Label(text=fname,fg=fclr,font=f)
    namelbl.place(x=295,y=530)
    header = Label(text=headtext,fg=fclr,font=f)
    header.place(x=295,y=8)
    namelbl = Label(text=fname,font=f,fg=fclr,background=txnc) #fname in another file(fname-->file name)
    namelbl.place(x=295,y=530)
    f1=open("bgclr.py","w")
    t2="txnc=['gray94']"
    f1.write(t2)
    f1.close()
#--------------------------------------------------------
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=text)
filemenu.add_command(label="Open", command=about)
filemenu.add_command(label="Save", command=abc)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=filemenu)

textcolor = Menu(menubar, tearoff=0)
textcolor.add_command(label="Black", command=txnblack)
textcolor.add_separator()
textcolor.add_command(label="Blue", command=txnblue)
textcolor.add_command(label="Green", command=txngreen)
textcolor.add_command(label="Red", command=txnred)
textcolor.add_command(label="Yellow", command=txnyellow)
menubar.add_cascade(label="Text Color", menu=textcolor)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Blue", command=blueback)
helpmenu.add_command(label="Default", command=default)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Background", menu=helpmenu)
root.config(menu=menubar)

frame = Frame(root, bg='green',background="black")
frame.pack(fill='x')
#----------------------------------------------------------
header = Label(text=headtext,font=f)
header.place(x=295,y=8)
#----------------------------------------------------------
extension = StringVar(root)
extension.set("txt") # default value
one = OptionMenu(root, extension,*valp)
one.place(x=430,y=554)
#----------------------------------------------------------
namelbl = Label(text=fname,font=f) #fname in another file(fname-->file name)
namelbl.place(x=295,y=530)
#----------------------------------------------------------
name = Entry(root,width="40",bd=4,textvariable="example",fg="black")
name.place(x=165,y=560)
#----------------------------------------------------------
text()
root.mainloop()
