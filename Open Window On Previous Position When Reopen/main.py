from tkinter import *
from tkinter import messagebox
try:
    from positionhistory import *
except:
    #if positionhistory file not present
    pass

try:
    x=position[0]
    y=position[1]
    z=position[2]
except:
    #if positionhistory file not present
    x=368
    y=132
    z=500

root=Tk()
root.geometry("700x%s+%s+%s"%(z,x,y))
root.iconbitmap("icon.ico")

def close():
    x=str(root.winfo_x())
    y=str(root.winfo_y())
    z=str(root.winfo_height())
    file=open("positionhistory.py","w")
    val="position=["+x+","+y+","+z+"]"
    file.write(val)
    file.close()
    root.destroy()
root.protocol("WM_DELETE_WINDOW",close)
