import re
from tkinter import *
from tkinter import messagebox
from time import *


def profile(email):
        username=email+".....Login at-"+ctime()
        loginpage.root.destroy()
        #-----PERMISSIONS-------------------------------------------
        def exitpermisstionlogin():
            if messagebox.askokcancel("Exit","Do you really want exit login page?"):
                    profile.new.destroy()
        def logout():
            if messagebox.askokcancel("Logout","Do you really want logout?"):
                        profile.new.destroy()
                        loginpage()
        #-----------------------------------------------------------
        profile.new=Tk()
        profile.new.title(username)
        profile.new.geometry("800x600+300+100")
        profile.new.resizable(False, True)
        labelshow=Label(profile.new,text="Successfully login",fg="green",font=('',30,'bold'))
        labelshow.place(x=230,y=50)
        #------------------------------------------------------------------
        def addnum():
            try:
                addnum.answerprint.destroy()
            except:
                pass
            num1=addnumkey.number1.get().strip()
            num2=addnumkey.number2.get().strip()
            result="NO"
            try:
                result=float(num1)+float(num2)
            except:
                msgnuminvalid=messagebox.showwarning("Invalid","Number's may be invalid please enter again")
                addnumkey()
            if result!="NO":
                addnum.answerprint=Label(profile.new,text="The sum is "+str(result),font=('',30,'bold'))
                addnum.answerprint.place(x=250,y=500)
        def addnumkey():
                number1text=Label(profile.new,text="Number 1:",fg="blue",font=('',40,'bold'))
                number1text.place(x=10,y=192)
                addnumkey.number1=Entry(profile.new,width=10,font=('',30))
                addnumkey.number1.place(x=280,y=200)

                addnumkey.number2=Entry(profile.new,width=10,font=('',30))
                addnumkey.number2.place(x=300,y=300)
                number1text=Label(profile.new,text=":Number 2",fg="blue",font=('',40,'bold'))
                number1text.place(x=530,y=290)

                buttonadd=Button(profile.new,text="ADD",width='40',bg='black',fg='white',font=('',20,'bold'),bd=4
                                 ,command=addnum)
                buttonadd.place(x=50,y=400)
        addnumkey()
        #---------------------------------------------------------------------------------------------------
        logout=Button(profile.new,text="Logout",command=logout,font=('',12),bd=4)
        logout.place(x=0,y=0)
        profile.new.protocol("WM_DELETE_WINDOW", exitpermisstionlogin)
        
        
def loginpage():
        loginpage.root=Tk()
        loginpage.root.geometry("800x600+300+100")
        loginpage.root.resizable(False, True)

        def login(event):
            print(event)
            email=logindetail.emailbox.get().lower().strip()
            password=logindetail.password.get()
            emailmatch = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
            if emailmatch:
                if password.strip()=='':
                    invalidpasswordmsg=messagebox.showwarning("Password Invalid","Please enter password.")
                elif len(password)<6:
                    invalidpasswordmsg=messagebox.showwarning("Password Invalid","Password is at lease 6 character long.")
                else:
                    if email!='a@a.com':
                         no_usermessage=messagebox.showwarning("No user found",'User "'+email+'" not found.')
                    else:
                        if password!='123456':
                            wrongpassword=messagebox.showwarning("Wrong password",'Password you enter is incorrect.')
                        else:
                            profile(email)  #login successful
                         
            else:
                if email=='':
                    invalidemail="Please enter email for login."
                    logindetail()
                else:
                    invalidemail='The email "'+email+'" is not valid.'
                    if invalidemail:
                        print("HELLO")
                invalidemailmsg=messagebox.showwarning("Invalid Email",invalidemail)


        def logindetail():
            emailtext=Label(loginpage.root,text="Email",font=('',40,'bold'))
            emailtext.place(x=315,y=80)
            logindetail.emailbox=Entry(loginpage.root,width=30,font=('',30))
            logindetail.emailbox.place(x=70,y=150)

            passwordtext=Label(loginpage.root,text="Password",font=('',40,'bold'))
            passwordtext.place(x=270,y=240)
            logindetail.password=Entry(loginpage.root,width=30,font=('',30))
            logindetail.password.config(show="*")
            logindetail.password.place(x=70,y=300)

        def exitpermission():
            if messagebox.askokcancel("Exit","Do you really want exit?"):
                loginpage.root.destroy()

        logindetail()

        loginbtn=Button(loginpage.root,text="LOGIN",font=('',20,'bold'),bd=5,command=login)
        loginbtn.place(x=330,y=370)
        loginpage.root.protocol("WM_DELETE_WINDOW", exitpermission)
loginpage()








