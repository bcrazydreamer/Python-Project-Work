#Devloped by Bharat Rawat
#For this install
#pip install pyqrcode
#pip install pypng

from tkinter import *
import PIL.Image
import PIL.ImageTk
import pyqrcode
from win32api import GetSystemMetrics

root = Tk()

root.geometry("500x600+388+132")
root.title("QR++")
try:
    root.iconbitmap('icon.ico')
except:
    pass
def clearfunction(): #Its help to clear previous pic from window
    try:
        showqr.label.destroy()
    except:
        pass #Initially no label so try
    try:
        welpic.destroy()
    except:
        pass
        
    qrcode()
    
def showqr():
    #Show genrated png image on label
    im = PIL.Image.open("QR-"+qrcode.x[0:12]+".png")
    photo = PIL.ImageTk.PhotoImage(im)
    showqr.label = Label(root, image=photo)
    showqr.label.image = photo
    showqr.label.pack()
    

def qrcode():
    qrcode.x=ent.get("1.0","end-1c")
    qr=pyqrcode.create(qrcode.x)
    #x[0:12]---> Its only take first 12 charecter or less as name of pic
    #Scale tends for size of pic
    if qrcode.x.strip()=="":
        qrcode.x="BlankQRCode"
    qr.png("QR-"+qrcode.x[0:12]+'.png',scale=4)
    if len(qrcode.x)>=600:
        root.state('zoomed')
        
    showqr()
def clear():
    ent.destroy()
        
head=Label(text="QR Code Genrator",height="1",width="20",font=("",20,"bold"))
head.pack()
ent=Text(height=2,width=30)
ent.pack()
#-------------------
saprator=Label()    #Saprator
saprator.pack()
#-------------------
btn=Button(text="Show",bd=4,width="20",command=clearfunction)
btn.pack()
#-------------------
saprator=Label()    #Saprator
saprator.pack()
#------------------

try:
    im = PIL.Image.open("welcome.png")
    photo = PIL.ImageTk.PhotoImage(im)
    welpic = Label(root, image=photo)
    welpic.image = photo
    welpic.pack()
except:
    welpic=Label(text="WELCOME",fg="green3",font=("",40,"bold"))
    welpic.pack()

root.mainloop()
