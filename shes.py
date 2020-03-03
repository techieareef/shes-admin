try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import tkinter as tk
from tkinter import messagebox
from utilities import write_log_file,log_except
import os
# import requests
import logging
from subprocess import Popen
import json
import sqlite3
from datetime import datetime
import time
from PIL import ImageTk, Image
backButton_height = 50
import commonFunction
import database_Server as db

root = tk.Tk()
root.resizable(width=True, height=True)


entry1=None;entry2=None;entry3=None;entry4=None;entry5=None
user=""
password=""
canvas1=None;canvas2=None;canvas3=None;canvas4=None;canvas5=None; canvas6=None; canvas=None
back=[]
login = 0
font_size = ('Verdana', 15)
dialog_button_font="Calibri 13 bold"
dialog_body_font="calibri 16"


def remove_shes_logs():
    import glob
    logging.info("Entered remove_shes_logs. ")
    with open('Const/config.json') as i:
        json_const = json.load(i)
        log_delete = json_const['LOG_DAYS']

    removed = 0
    #path = "desired path"
    # Check current working directory.
    dir_to_search = os.getcwd()

    if dir_to_search != "/Log/":  # compare current to desired directory
        # Now change the directory
        os.chdir('Log/')
        # Check current working directory.
        dir_to_search = os.getcwd()

    tifCounter = len(glob.glob1(dir_to_search, "*.log"))
    logging.info("Number of log files in directory : " + str(tifCounter))

    dataset_path = 'Log/'
    files = glob.glob(dir_to_search + "*.log")

    if tifCounter > log_delete:
        for dirpath, dirnames, filenames in os.walk(dir_to_search):
            filenames.sort(key=os.path.getmtime)

            for file in filenames[-len(filenames):-1]:

                curpath = os.path.join(dirpath, file)

                log_delete = json_const['LOG_DAYS']
                if len(glob.glob1(dir_to_search, "*.log")) > log_delete:

                    os.remove(curpath)
                    logging.info("Deleted log file : " + str(file))
                    removed += 1

    logging.info("Number of log files removed : " + str(removed))

def backpage():
    global back,root
    if len(back)>0 :
        v=back[-1]
        back=back[:-1]
        if v==1:
            homemiddlepart(user)
        #     initialmiddlepart()
        elif v==2:
            homemiddlepart(user)
        elif v==3:
          loginPage()
        # elif v==4:
        #     if canvas5 is not None:
        #         canvas5.config(height=0, width=0)
        #         canvas5.delete("all")
        #     gamepage()
        # elif v==5:
        #     reportGameGraph.destroy()
        #     runreport()

    else:
        # if messagebox.askyesno("Verify", "Do you want to exit?")==True :
            root.quit()

try:

    imgpath = "Pictures/login.png"
    img = Image.open("Pictures/login.png")
    # img=img.resize((1390, 770), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)

    image2 = Image.open("Pictures/soujhe_logo.png")
    image2 = image2.resize((150, 150), Image.ANTIALIAS)
    photo_image2 = ImageTk.PhotoImage(image2)
    image3 = Image.open("Pictures/company_logo.png")
    image3 = image3.resize((150, 120), Image.ANTIALIAS)
    photo_image3 = ImageTk.PhotoImage(image3)
    image4 = Image.open("Pictures/reports-png-1.png")
    image4 = image4.resize((150, 150), Image.ANTIALIAS)
    report_image= ImageTk.PhotoImage(image4)
    image6 = Image.open("Pictures/signout.png")
    image6 = image6.resize((150, 150), Image.ANTIALIAS)
    photo_image6 = ImageTk.PhotoImage(image6)
    image7 = Image.open("Pictures/homeicon.jpg")
    image7 = image7.resize((150, 150), Image.ANTIALIAS)
    photo_image7 = ImageTk.PhotoImage(image7)
    image13 = Image.open("Pictures/admin.png")
    image13 = image6.resize((30, 30), Image.ANTIALIAS)
    photo_image13 = ImageTk.PhotoImage(image13)
    image17 = Image.open("Pictures/patient_reg.png")
    image17 = image17.resize((170, 170), Image.ANTIALIAS)
    doctor_image = ImageTk.PhotoImage(image17)
    image9 = Image.open("Pictures/backbuttonicon.png")
    image9 = image9.resize((90, 90), Image.ANTIALIAS)
    photo_image9 = ImageTk.PhotoImage(image9)
    # spinnerwheel = spinningGIF.Spinner(root, size=64)
    # canvas2.create_window(int(root.winfo_screenwidth() / 2 - 50), int(root.winfo_screenheight() / 2 - 50),
    #                       window=spinnerwheel)
except:
    log_except()
    #pass

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

def loginPage():
    global entry3,entry4,canvas

    if canvas1 is not None:
        canvas1.config(height=0, width=0)
        canvas1.delete("all")
    if canvas5 is not None:
        canvas5.config(height=0, width=0)
        canvas5.delete("all")
    if canvas4 is not None:
        canvas4.config(height=0, width=0)
        canvas4.delete("all")
    if canvas2 is not None:
        canvas2.config(height=0, width=0)
        canvas2.delete("all")
    if canvas is not None:
        canvas.destroy()
    screenheight = root.winfo_screenheight()
    screenWidgth = root.winfo_screenwidth()
    canvas = tk.Canvas(root, width=screenWidgth, height=screenheight, bd=0, highlightthickness=0)
    canvas.create_image(screenWidgth / 2, screenheight / 2, image=photo)
    canvas.pack()

    userid = tk.StringVar()
    password=tk.StringVar()

    entry3 =Entry(canvas, textvariable=userid, bd=3, width=20, font=("Purisa", 14))
    entry3.place(x=300, y=330)
    entry3.focus_set()
    entry3.delete(0, END)

    entry4 =Entry(canvas,show="*", textvariable=password, bd=3, width=20, font=("Purisa", 14))
    entry4.place(x=300, y=410)

    entry4.focus_set()
    button1 = Button(canvas, text="Login",bg="white",activebackground="blue",font=('Helvetica', '15'),
                          width=10,cursor="hand2",command=checkLogIn)
    button1.place(x=230, y=490)

    regi_but = Button(canvas, text="Register", bg="white", activebackground="blue", font=('Helvetica', '15'),
                     width=10, cursor="hand2",command=registration)
    regi_but.place(x=360, y=490)
    # forgot_label = Label(canvas, font="Times 13", text="forgot password", bg="white",
    #                   fg="blue",)
    # forgot_label.place(x=250,y=550)

def checkLogIn() :
    global username, password, login,entry3,entry4

    username=actNum = entry3.get()
    pinNum = entry4.get()

    if db._logincheck({'ship_name' : username,'sys_pwd' : commonFunction.computeMD5hash(pinNum)}):
        logging.info("Valid Login Credentials - " + str(time.strftime('%d %b %Y %X')) )
        homemiddlepart(user=actNum)
    elif actNum == "":
        logging.info(str(time.time()) + " " + "Please enter username")
        d = dialoguebox(root, text="Please enter a valid User ID", buttons=["OK"], default=0, cancel=2,
                        title='warn',
                        icon='Pictures/warn.png')
        d.go()
    elif pinNum == "":
        logging.info(str(time.time()) + " " + "Please enter password")

        d = dialoguebox(root, text="Please enter password.", buttons=["OK"], default=0, cancel=2, title='warn',
                        icon='Pictures/warn.png')
        d.go()
    else:
        d = dialoguebox(root, text="User ID or Password is incorrect", buttons=["OK"], default=0, cancel=2,
                        title="warn", icon='Pictures/warn.png')
        d.go()

class dialoguebox:

    def __init__(self, master,
                 text='', buttons=[], default=None, cancel=None,title=None, class_=None,icon=None):
        if class_:
            self.root = Toplevel(master, class_=class_)
        else:
            self.root = Toplevel(master)
        if title:
            self.root.title(title)
            self.root.iconname(title)


        self.message = Message(self.root, text=text,aspect=700,font=dialog_body_font,bg="white")
        self.message.pack(expand=True, fill=BOTH)
        self.frame =tk.Frame(self.root)
        self.frame.pack(fill='both',expand=0)
        self.num = default
        self.cancel = cancel
        self.default = default
        self.root.bind('<Return>', self.return_event)
        for num in range(len(buttons)):
            s = buttons[num]
            b = Button(self.frame, text=s,command=(lambda self=self, num=num: self.done(num)),bg="#007ED9",fg="white",borderwidth=1,font=dialog_button_font,width=10,activebackground='blue',
                                         cursor="hand2")

            # infuture we need more buttons to add in popup disable from add belo code and remove the ****to **** code in comments
            # b = Button(self.frame, text=s,
            #            command=(lambda self=self, num=num: self.done(num)), bg="#007ED9", fg="white", borderwidth=2,
            #            width=6, font="Times 15 bold")
            # if num == default:
            #     b.config(relief=RAISED, borderwidth=2, bg="#007ED9")
            # b.pack(side=LEFT, expand=1, padx=10, pady=10)
            # *************
            if num == default:
                b.config(relief=RAISED, borderwidth=1)
                b.pack(pady=10)
            else:
                b.place(x=270,y=10)

        self.root.protocol('WM_DELETE_WINDOW', self.wm_delete_window)
        self._set_transient(master,icon)

    def _set_transient(self, master,icon, relx=0.45, rely=0.4):
        widget = self.root
        widget.withdraw() # Remain invisible while we figure out the geometry
        widget.transient(master)
        widget.update_idletasks()
        # Actualize geometry information
        widget.geometry('400x200')
        if master.winfo_ismapped():
            m_width = master.winfo_width()
            m_height = master.winfo_height()
            m_x = master.winfo_rootx()
            m_y = master.winfo_rooty()
        else:
            m_width = master.winfo_screenwidth()
            m_height = master.winfo_screenheight()
            m_x = m_y = 0
        w_width = widget.winfo_reqwidth()
        w_height = widget.winfo_reqheight()
        x = m_x + (m_width - w_width) * relx
        y = m_y + (m_height - w_height) * rely
        if x+w_width > master.winfo_screenwidth():
            x = master.winfo_screenwidth() - w_width
        elif x < 0:
            x = 0
        if y+w_height > master.winfo_screenheight():
            y = master.winfo_screenheight() - w_height
        elif y < 0:
            y = 0

        widget.geometry("+%d+%d" % (x, y))
        img = PhotoImage(file=icon)
        widget.tk.call('wm', 'iconphoto', widget._w, img)
        widget.deiconify() # Become visible at the desired location

    def go(self):
        self.root.wait_visibility()
        self.root.grab_set()
        self.root.mainloop()
        self.root.destroy()
        return self.num

    def return_event(self, event):
        if self.default is None:
            self.root.bell()
        else:
            self.done(self.default)

    def wm_delete_window(self):
        if self.cancel is None:
            self.root.bell()
        else:
            self.done(self.cancel)

    def done(self, num):
        self.num = num
        self.root.quit()

def homemiddlepart(user) :
    try:

        global canvas5, report_image,image2, canvas4, canvas1, \
            login, back, photo_image6, reportGameGraph, canvas2
        # back.append(1)
        if canvas1 is not None:
            canvas1.config(height=0, width=0)
            canvas1.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if canvas2 is not None:
            canvas2.config(height=0, width=0)
            canvas2.delete("all")

        if canvas is not None:
            canvas.destroy()
        login = 1
        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="Home")

        canvas2 = Canvas(root, bg="white", width=root.winfo_screenwidth() - 40, height=root.winfo_screenheight() - 165,
                         highlightbackground="blue", highlightthickness=20)
        canvas2.place(x=0, y=30)

        # Images
        canvas2.create_image(150, 100, image=photo_image2)
        canvas4 = Canvas(root, bg="white", width=230, height=200,
                         highlightthickness=0)  # highlightbackground="black",highlightthickness=5)
        canvas4.place(x=root.winfo_screenwidth() - 270, y=50)
        canvas4.create_text(80, 25, fill="black", font="Times 14 bold", text="Login : ")
        canvas4.create_text(140, 25, fill="blue", font="Times 14 bold ", text=str(user).title())
        image6 = Image.open("Pictures/signout.png")
        image6 = image6.resize((30, 30), Image.ANTIALIAS)
        photo_image6 = ImageTk.PhotoImage(image6)
        button1 = HoverButton(canvas4, compound=TOP, bg="black", image=photo_image6, borderwidth=0,command=loginPage)
        button1.place(x=120, y=50)

        canvas5 = Canvas(root, bg="white", width=1100, height=350, bd=0, relief='ridge',highlightthickness=0)
        canvas5.place(x=100, y=200)

        canvas5.create_text(450, 90, fill="black", font="Times 20 italic bold", text="Doctor Request")
        canvas5.create_text(720, 90, fill="black", font="Times 20 italic bold", text="Report")

        doctor_img = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=doctor_image,
                              borderwidth=0,  cursor="hand2")#command=gamepage,
        doctor_img.place(x=370, y=140)
        report_img = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=report_image,
                              borderwidth=0, cursor="hand2")  # command=lambda:runreport()
        report_img.place(x=640, y=140)  # x=790, y=140
        # ========================
    except:
        log_except()

def toprightmostpart() :
    try:

        global canvas4, username, photo_image6, photo_image7,login
        if login == 0:
            if canvas4 is not None:
                canvas4.config(height=0, width=0)
                canvas4.delete("all")
        elif login == 1:
            if canvas4 is not None:
                canvas4.config(height=0, width=0)
                canvas4.delete("all")
            canvas4 = Canvas(root, bg="white", width=230, height=100,
                             highlightthickness=0)  # highlightbackground="black",highlightthickness=5)
            canvas4.place(x=root.winfo_screenwidth() - 270, y=50)
            canvas4.create_text(80, 25, fill="black", font="Times 14 bold", text="Login : ")
            canvas4.create_text(140, 25, fill="blue", font="Times 14 bold ", text=str(user).title())
            image6 = Image.open("Pictures/signout.png")
            image6 = image6.resize((30, 30), Image.ANTIALIAS)
            photo_image6 = ImageTk.PhotoImage(image6)
            button1 = HoverButton(canvas4, compound=TOP, bg="black", image=photo_image6, borderwidth=0,
                                  command=homemiddlepart(user), activebackground='blue', cursor="hand2")

            button1.place(x=120, y=50)

            image7 = Image.open("Pictures/homeicon.jpg")
            image7 = image7.resize((30, 30), Image.ANTIALIAS)
            photo_image7 = ImageTk.PhotoImage(image7)
            button2 = HoverButton(canvas4, compound=TOP, fg="white", bg="black", image=photo_image7, borderwidth=0,
                                  command=lambda: homemiddlepart(user), activebackground='blue', cursor="hand2")
            button2.place(x=60, y=50)
    except:
        log_except()

def registration():
    try:

        global canvas5,canvas2, canvas4,canvas1, back,ship_entry,\
            cap_phone_entry,ship_email_entry, ship_email_pwd_entry,login_pwd_entry,label_msg
        back.append(3)
        # if canvas1 is not None:
        #     canvas1.config(height=0, width=0)
        #     canvas1.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")


        if canvas is not None:
            canvas.destroy()

        if canvas5 is not None:
            canvas5.destroy()
        login = 1
        ship_name = StringVar()
        cap_phone = StringVar()
        ship_email = StringVar()
        ship_email_pwd = StringVar()
        login_pwd = StringVar()

        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="Registration")

        #toprightmostpart()

        canvas5 = Canvas(root, bg="white", width=1000, height=500, bd=0, relief='ridge',
                         highlightthickness=0)

        canvas5.place(x=200, y=200)

        label_msg = Label(canvas5, font="Times 13", text="", bg="white",
                          fg="blue", width=50)
        label_msg.place(x=180, y=35)
        canvas5.create_text(180, 80, fill="black", font="Times 20 italic bold", text="Ship Name*           : ")
        canvas5.create_text(180, 160, fill="black", font="Times 20 italic bold", text="Phone            : ")
        canvas5.create_text(180, 240, fill="black", font="Times 20 italic bold", text="Email ID*            : ")
        canvas5.create_text(180, 300, fill="black", font="Times 20 italic bold", text="Email Password*      : ")
        canvas5.create_text(180, 380, fill="black", font="Times 20 italic bold", text="Login Password*      : ")

        ship_entry = Entry(canvas5, textvariable=ship_name, bd=3, width=11, font=font_size, validate="key")
        ship_entry.place(x=360, y=70)
        cap_phone_entry = Entry(canvas5, textvariable=cap_phone, bd=3, width=11, font=font_size, validate="key")
        cap_phone_entry.place(x=360, y=140)
        ship_email_entry = Entry(canvas5, textvariable=ship_email, bd=3, width=11, font=font_size, validate="key")
        ship_email_entry.place(x=360, y=210)
        ship_email_pwd_entry = Entry(canvas5,show="*", textvariable=ship_email_pwd, bd=3, width=11, font=font_size,
                                     validate="key")
        ship_email_pwd_entry.place(x=360, y=280)
        login_pwd_entry = Entry(canvas5,show="*", textvariable=login_pwd, bd=3, width=11, font=font_size,
                                     validate="key")
        login_pwd_entry.place(x=360, y=350)
        save_button = HoverButton(canvas5, text="Save", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                  width=15, command=lambda: saveDetails(), activebackground='blue', cursor="hand2")
        save_button.place(x=180, y=420)

        back_button = HoverButton(canvas6, image=photo_image9, width=90, height=backButton_height, bg="white",
                                  borderwidth=0,
                                  font=('Helvetica', '15'), command=backpage, cursor="hand2")
        back_button.place(x=50, y=580)

        back_button = HoverButton(canvas6, image=photo_image9,width=90,
                                  height=backButton_height, bg="white",activebackground='white', borderwidth=0,
                              font=('Helvetica', '15'), command=backpage, cursor="hand2")
        back_button.place(x=50, y=580)

    except:
        log_except()

def saveDetails():
    print("in save method")
    ship_name= ship_entry.get()
    cap_phone= cap_phone_entry.get()
    ship_email= ship_email_entry.get()
    ship_email_pwd= ship_email_pwd_entry.get()
    lpgin_pwd= login_pwd_entry.get()

    if ship_name and ship_email and ship_email_pwd and lpgin_pwd:
        if db._detailscheck(ship_name, ship_email):
            email_content = {
                'ship_name': ship_name,
                'cap_phone': cap_phone,
                'ship_email': ship_email,
                'ship_email_pwd': ship_email_pwd,
                'lpgin_pwd': lpgin_pwd
            }
            # email send
            SuccessMsg = commonFunction._sendregemail(email_content)
            if type(SuccessMsg) is bool:
                label_msg.config(text="Registration Done")
                loginPage()
            else:
                label_msg.config(text=SuccessMsg)
        else:
            label_msg.config(text="Ship Name/Email Already Exist")

    elif ship_name == "":
        logging.info(str(time.time()) + " " + "Please Enter Ship Name")
        d = dialoguebox(root, text="Please enter Ship Name", buttons=["OK"], default=0, cancel=2,
                        title='warn',
                        icon='Pictures/warn.png')
        d.go()
    elif ship_email == "":
        logging.info(str(time.time()) + " " + "Please Enter Ship Email")

        d = dialoguebox(root, text="Please Enter Ship Email.", buttons=["OK"], default=0, cancel=2, title='warn',
                        icon='Pictures/warn.png')
        d.go()
    elif ship_email_pwd =="":
        d = dialoguebox(root, text="Please Enter Ship Email Password", buttons=["OK"], default=0, cancel=2,
                        title="warn", icon='Pictures/warn.png')
        d.go()
    elif lpgin_pwd == "":
        d = dialoguebox(root, text="Please Enter Password", buttons=["OK"], default=0, cancel=2,
                        title="warn", icon='Pictures/warn.png')
        d.go()


loginPage()
# create a clickable button on the canvas
root.state('zoomed')
root.mainloop()