from tkinter import *
import urllib.request, urllib.parse, urllib.error
import lxml.html
import requests
import timeit
import timeit
import html5lib
from bs4 import BeautifulSoup
import re
import webbrowser
import csv
root=Tk()
root.geometry("1200x600")
root.state('zoomed')
root.title("Search Engine")


def ShowResult(database,search,status):
            try:
                ShowResult.scrollbar.destroy()
            except:
                pass
            ShowResult.scrollbar = Scrollbar(root)
            ShowResult.scrollbar.pack(side=LEFT, fill=Y)

            listbox = Listbox(root,width=135, height=28,font=("",15))
            listbox.place(x=30,y=90)

            for item in database:
                ShowResult.notfound=1
                if(item!=search):
                    listbox.insert(END, item)
                    ShowResult.notfound=0
                    
            if ShowResult.notfound==1:# Agar koi link nai mila #Count oprations
                ShowResult.countlink=0
                listbox.insert(END,"Not found")
            else:
                if createlist.flag==0: #Data base me save karega
                    ShowResult.countlink=len(database)-1
                else:
                    ShowResult.countlink=len(database)
                
            ShowResult.stop = timeit.default_timer() #Time
             
            if status==1: #database me value store karega lega
                if len(search)>0 and ShowResult.notfound==0:
                    with open(r'database.csv', 'a',newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(database)
                    ShowResult.stop = timeit.default_timer() #Time
                    
            #------------------------TIME------------------------------------
            ShowResult.exitime=(ShowResult.stop - createlist.start) #Search Time Final
            ShowResult.exitime="Search in "+str(round(ShowResult.exitime,4))+" Second"
            try:
                ShowResult.timeshow.destroy()
            except:
                pass
            try:
                ShowResult.countlinklabel.destroy()
            except:
                pass
            #----------------
            ShowResult.timeshow=Label(root,text=ShowResult.exitime,font=("",10,"bold"))
            ShowResult.timeshow.place(x=0,y=0)
            #-----------------------Link Count-------------------------------
            ShowResult.countlink="There are "+str(ShowResult.countlink)+" links to show"
            ShowResult.countlinklabel=Label(root,text=ShowResult.countlink,font=("",15,"bold"))
            ShowResult.countlinklabel.place(x=0,y=20)
            #----------------------------------------------------------------
            listbox.config(yscrollcommand=ShowResult.scrollbar.set)
            ShowResult.scrollbar.config(command=listbox.yview)
            ShowResult.f=0
            def openweb(event):
                url=listbox.get(ACTIVE)
                if(len(database)>1):
                    try:
                        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
                    except:
                        webbrowser.open(url)
            def do(event):
                    if ShowResult.f==1:
                        do.lineshow.destroy()
                    value=str((listbox.get(ACTIVE)))
                    do.lineshow=Label(root,text=value,fg="blue",font=("",15,"bold"))
                    do.lineshow.place(x=20,y=770)
                    ShowResult.f=1
                    
            callback = lambda event: do(event)
            callback2 = lambda event: openweb(event)
            
            listbox.bind("<Button-1>", callback)
            listbox.bind("<Double-Button-1>", callback2)

#-------------------------------------------------------------------------------------------------
def createlist():
    createlist.start = timeit.default_timer() #Time start-----------START
    search=X.get().strip().lower()
    try:
        DatabaseCheck = open('database.csv')
        DatabaseReader = csv.reader(DatabaseCheck)
        DatabaseData = list(DatabaseReader)
    except:
        DatabaseCheck = open('database.csv', 'w')
    createlist.flag=0
    database=[]
    status=0 #To check ki database me save karna hai ya nai
    for item in DatabaseData:
        if item[0]==search:
            for i in range(1,len(item)):
                database.append(item[i])
                createlist.flag=1
    #------------------------------------------------------------------------
    if createlist.flag==1: #Database me hai
        status=0
        ShowResult(database,search,status)
    if createlist.flag==0:  #Data base me save karega   
        results=100
        if(len(search)>0):
            database.append(search)
        start = timeit.default_timer()
        page = requests.get("https://www.google.com/search?q={}&num={}".format(search, results))
        soup = BeautifulSoup(page.content, "html5lib")
        links = soup.findAll("a")
        for link in links :
            link_href = link.get('href')
            if "url?q=" in link_href and not "webcache" in link_href:
                mysearch=link.get('href').split("?q=")[1].split("&sa=U")[0]
                database.append(mysearch)
        if(len(database)==1):#Blank Show Karne k liye
            database=["Search box Should not be blank"]
        status=1
        ShowResult(database,search,status)



        

label=Label(root,text="Welcome to Search Engine",font=("",15))
label.pack()
X=Entry(root,width=40,font=("",15))
X.pack()
show=Button(root,text="Submit",command=createlist)
show.pack()
