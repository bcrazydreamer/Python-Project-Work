from tkinter import *
from tkinter import filedialog
import pygame
import os
from tkinter import ttk
from PIL import ImageTk

pygame.init()
pygame.mixer.init()
root=Tk()
root.geometry("500x500")
root.minsize(width=500, height=500)
#root.resizable(False, False)
root.title("DMusic")
root.iconbitmap(r'img/icon/icon.ico')
root.config(background="white")
ttk.Separator(root).place(x=0, y=15, relwidth=1)

class display:
    def initial_screen(self):
        if(root.winfo_width()>700):
            w=int(root.winfo_width()/10)-16
        
        else:
            w=int(root.winfo_width()/10)-10
        display_ob.frame = Frame(root)
        display_ob.frame.place(relx=0.5, rely=0.29,anchor=CENTER)
        listbox = Listbox(display_ob.frame,width=w, height=10,
                          font=("",15),fg="white",bg="black")
        listbox.pack(side = 'left',fill = 'x' )
    #-------------------------------------------------------
    def songs_screen(self,database):
        try:
            display_ob.frame.destroy()
        except:
            pass
        if(root.winfo_width()>700):
            w=int(root.winfo_width()/10)-16
        else:
            w=int(root.winfo_width()/10)-10
        display_ob.frame = Frame(root)
        display_ob.frame.place(relx=0.5, rely=0.29,anchor=CENTER)
        h=int(root.winfo_height()/50)
        display_ob.listbox = Listbox(display_ob.frame,width=w, height=h,font=("",15),fg="white",bg="black")
        display_ob.listbox.pack(side = 'left',fill = 'x' )
        scrollbar = Scrollbar(display_ob.frame, orient="vertical",command=display_ob.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        display_ob.listbox.config(yscrollcommand=scrollbar.set)
        for item in database:
            if(item!=''):
                display_ob.listbox.insert(END, item)
        display_ob.listbox.selection_set( first = 0 )

    

class actions:
    def file(self):
        get=Tk()
        get.withdraw()
        database=[]
        try:
            screen_ob.select = filedialog.askdirectory()
            arr = os.listdir(screen_ob.select)
            for i in range(len(arr)):
                if arr[i].endswith('.mp3') or arr[i].endswith('.mid') or arr[i].endswith('.wav'):
                    database.append(arr[i])
                    screen_ob.flag_file=True
            if len(database)==0:
                screen_ob.flag=False
                database.append("There are no any music file.")
        except:
            screen_ob.flag_file=False
            database.append("Please select any music folder.")
        display_ob.songs_screen(database)
        
    def play(self):
        if(screen_ob.flag_file):
            play.config(bg='gray')
            stop.config(bg='white')
            pause.config(bg='white')
        else:
            play.config(bg='white')
           
        if(screen_ob.pause_status):
            pygame.mixer.music.unpause() #If any song is pause
            screen_ob.pause_status=False
        else:
            try:
                filename=display_ob.listbox.get(ACTIVE)
                filename=screen_ob.select+'/'+filename
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()
            except:
                database=["Please select any music first"]
                display_ob.songs_screen(database)
                
    def pause(self):
        if(pygame.mixer.music.get_busy()==1):
            play.config(bg='white')
            stop.config(bg='white')
            pause.config(bg='gray')
            pygame.mixer.music.pause()
            screen_ob.pause_status=True

        
    def stop(self):
        if(pygame.mixer.music.get_busy()==1):
            pygame.mixer.music.stop()
            play.config(bg='white')
            pause.config(bg='white')
            stop.config(bg='gray')
    def close(self):
        if(pygame.mixer.music.get_busy()==1):
            pygame.mixer.music.stop()
        root.destroy()
        root.quit()
#-------------------------------------------------------------------------
    def volup(self):
        try:
           screen_ob.vollbl.destroy()
        except:
            pass
        if(screen_ob.value<10):
            screen_ob.value=screen_ob.value+1
        else:
            screen_ob.value=10
        #--Unmute the icon if that is muted----------------
        screen_ob.mutestatus=False
        buttons_ob.mute_btn.destroy()
        mute_btn=Button(root,command=screen_ob.mute)
        image = ImageTk.PhotoImage(file="img/unmute.png")
        mute_btn.config(image=image,bg='white',bd=0)
        mute_btn.image = image
        mute_btn.place(relx=0.95, rely=0.95,anchor=CENTER)
        #--------------------------------------------------
        pygame.mixer.music.set_volume(screen_ob.value/10)
        screen_ob.vollbl=Label( root, text=screen_ob.value,bg='white',
                                fg='black',font=('times', 20, 'bold') )
        screen_ob.vollbl.place(relx=0.15, rely=0.95,anchor=CENTER)
    def voldown(self):
        try:
           screen_ob.vollbl.destroy()
        except:
            pass
        if(screen_ob.value>0):
            screen_ob.value=screen_ob.value-1
        else:
            screen_ob.value=0
        #--Unmute the icon if that is muted----------------
        screen_ob.mutestatus=False
        buttons_ob.mute_btn.destroy()
        mute_btn=Button(root,command=screen_ob.mute)
        image = ImageTk.PhotoImage(file="img/unmute.png")
        mute_btn.config(image=image,bg='white',bd=0)
        mute_btn.image = image
        mute_btn.place(relx=0.95, rely=0.95,anchor=CENTER)
        #--------------------------------------------------
        pygame.mixer.music.set_volume(screen_ob.value/10)
        screen_ob.vollbl=Label( root, text=screen_ob.value,bg='white',
                                fg='black',font=('times', 20, 'bold') )
        screen_ob.vollbl.place(relx=0.15, rely=0.95,anchor=CENTER)
    def mute(self):
        screen_ob.temp=screen_ob.value/10
        if(screen_ob.mutestatus):
            pygame.mixer.music.set_volume(screen_ob.temp)
            screen_ob.mutestatus=False
            buttons_ob.mute_btn.destroy()
            mute_btn=Button(root,command=screen_ob.mute)
            image = ImageTk.PhotoImage(file="img/unmute.png")
            mute_btn.config(image=image,bg='white',bd=0)
            mute_btn.image = image
            mute_btn.place(relx=0.95, rely=0.95,anchor=CENTER)
        else:
            pygame.mixer.music.set_volume(0)
            screen_ob.mutestatus=True
            buttons_ob.mute_btn.destroy()
            buttons_ob.mute_btn=Button(root,command=screen_ob.mute)
            image = ImageTk.PhotoImage(file="img/mute.png")
            buttons_ob.mute_btn.config(image=image,bg='white',bd=0)
            buttons_ob.mute_btn.image = image
            buttons_ob.mute_btn.place(relx=0.95, rely=0.95,anchor=CENTER)
#-------------------------------------------------------------------------            
class buttons:
    def mute(self):
        buttons_ob.mute_btn=Button(root,command=screen_ob.mute)
        image = ImageTk.PhotoImage(file="img/unmute.png")
        buttons_ob.mute_btn.config(image=image,bg='white',bd=0)
        buttons_ob.mute_btn.image = image
        buttons_ob.mute_btn.place(relx=0.95, rely=0.95,anchor=CENTER)
#------------------------------------------------------------------------------------------
display_ob=display()
buttons_ob=buttons()
screen_ob=actions()
buttons_ob.mute()
display_ob.initial_screen()
#-----------------------Initialize------------------------
screen_ob.value=10
screen_ob.flag_file=False #No music selected
screen_ob.mutestatus=False
screen_ob.vollbl=Label( root, text=screen_ob.value,bg='white',
                        fg='black',font=('times', 20, 'bold') )
screen_ob.vollbl.place(relx=0.15, rely=0.95,anchor=CENTER)
screen_ob.pause_status=False
#root.bind('<Configure>', lambda e: ob.initial_screen())

#-------------------------------------------------------------------------                
ttk.Separator(root).place(relx=0, rely=0.55, relwidth=1)
#------------------Play-----------------------------------
play=Button(root,command=screen_ob.play)
image = ImageTk.PhotoImage(file="img/play.png")
play.config(image=image,bg='white',bd=0)
play.image = image
play.place(relx=0.5, rely=0.65,anchor=CENTER)
#------------------Pause----------------------------------
pause=Button(root,command=screen_ob.pause)
image = ImageTk.PhotoImage(file="img/pause.png")
pause.config(image=image,bg='white',bd=0)
pause.image = image
pause.place(relx=0.3, rely=0.65,anchor=CENTER)
#------------------Stop-----------------------------------
stop=Button(root,command=screen_ob.stop)
image = ImageTk.PhotoImage(file="img/stop.png")
stop.config(image=image,bg='white',bd=0)
stop.image = image
stop.place(relx=0.7, rely=0.65,anchor=CENTER)
#---------------------------------------------------------
ttk.Separator(root).place(relx=0, rely=0.85, relwidth=1)
#------------------File-----------------------------------
btn1=Button(root,command=screen_ob.file)
image = ImageTk.PhotoImage(file="img/file.png")
btn1.config(image=image,bg='white',bd=0)
btn1.image = image
btn1.place(relx=0.5, rely=0.93,anchor=CENTER)
#----------------VolumeUp---------------------------------
vol_u=Button(root,command=screen_ob.volup)
image = ImageTk.PhotoImage(file="img/volup.png")
vol_u.config(image=image,bg='white',bd=0)
vol_u.image = image
vol_u.place(relx=0.05, rely=0.95,anchor=CENTER)
#----------------VolumeDown-------------------------------
vol_d=Button(root,command=screen_ob.voldown)
image = ImageTk.PhotoImage(file="img/voldown.png")
vol_d.config(image=image,bg='white',bd=0)
vol_d.image = image
vol_d.place(relx=0.25, rely=0.95,anchor=CENTER)
#---------------------------------------------------------
root.protocol("WM_DELETE_WINDOW", screen_ob.close)
root.mainloop()
          



