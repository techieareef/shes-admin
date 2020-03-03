import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
import platform
import time
import os

import logging
import json
from PIL import Image, ImageTk
import database_Server as db
import commonFunction
from utilities import write_log_file,log_except



l=0
reg_text_size="Times 15 italic bold"
name=""
username=""
password=""
username2=""
password2=""
password3=""
access=""
patientid=""
patientids=""
reportStart=""
reportEnd=""
back=[]
patient_entry=""
button2=None
numberChoosen=None
key=None
numberChoosen1=None
entry1=None;entry2=None;entry3=None;entry4=None;entry5=None;entry_config=None;license_entry=None;disorder_entry=None;report_entry=None
canvas1=None;canvas2=None;canvas3=None;canvas4=None;canvas5=None; canvas6=None;canvas=None
login=0
font_size = ('Verdana', 15)
root = Tk()
root.title('Seaferers Health Expert System')

if platform.system()=="Linux":
    root.attributes('-zoomed', True)
    backButton_height = 90
else:
    root.state('zoomed')
    backButton_height = 50
s = ttk.Style(root)
dialog_button_font="Calibri 13 bold"
dialog_body_font="calibri 16"
status=""
excategory=""
optionChoosen=''
text=""
lable_font="Times 20 italic bold"

ExerciseName=''
info="                                                Information       "
warn = "                                   Warning       "
error="                                                Error"


image3 = Image.open("Pictures/company_logo.jpg")
image3 = image3.resize((200, 140), Image.ANTIALIAS)
photo_image3 = ImageTk.PhotoImage(image3)
image4 = Image.open("Pictures/reports-png-1.png")
image4 = image4.resize((170, 170), Image.ANTIALIAS)
report_image = ImageTk.PhotoImage(image4)
image7 = Image.open("Pictures/homeicon.jpg")
image7 = image7.resize((150, 150), Image.ANTIALIAS)
photo_image7 = ImageTk.PhotoImage(image7)
image9 = Image.open("Pictures/backbuttonicon.png")
image9 = image9.resize((90, 90), Image.ANTIALIAS)
photo_image9 = ImageTk.PhotoImage(image9)
image17 = Image.open("Pictures/patient_reg.png")
image17 = image17.resize((170, 170), Image.ANTIALIAS)
doctor_image = ImageTk.PhotoImage(image17)

def create_shes_logs ():
    from pathlib import Path
    cdir = os.path.abspath(os.path.dirname(__file__))
    if (platform.system() == "Linux"):
        dirnew = cdir + '/Log'
    else:
        dirnew = cdir + '\\Log'
    p = Path(dirnew)

    if not ( p.exists() and p.is_dir()): # create Log dir if one does not exist
        os.makedirs(dirnew)

    # Log Initilization
    write_log_file()
    logging.info("========================================================")
    logging.info('                   Session Started                      ')
    logging.info("========================================================")
create_shes_logs()
#++++++++++++backbutton functionality+++++++++++
def backpage():
    global back,root
    if len(back)>0 :
        v=back[-1]
        back=back[:-1]
        if v==1:
            #homemiddlepart(user)
        #     initialmiddlepart()
            pass
        elif v==2:
            # homemiddlepart(user)
            pass
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


# +++++++++++++++++Custom Dialog box changes++++++++++++++++++++++
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
            b =Button(self.frame, text=s,command=(lambda self=self, num=num: self.done(num)),bg="#007ED9",fg="white",borderwidth=1,width=10,font=dialog_button_font,activebackground='blue',
                                         cursor="hand2")

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
        # self.root.mainloop()
        self.root.wait_window()
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
        self.root.destroy()
# ++++++++++++++++++++++Custom Dialog box ended+++++++++++++++++++++++



# +++++++++++++++++++++HoverButton +++++++++++++++++++
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

# +++++++++++++++++HoverButton Ended+++++++++++++++++++++++
def toprightmostpart() :
    try:

        global canvas4, username, photo_image6, photo_image7, photo_image8, login

        if login == 0:
            if canvas4 is not None:
                canvas4.config(height=0, width=0)
                canvas4.delete("all")
        elif login == 2:

            if canvas4 is not None:
                canvas4.config(height=0, width=0)
                canvas4.delete("all")
            canvas4 = Canvas(root, bg="white", width=230, height=100,
                             highlightthickness=0)  # highlightbackground="black",highlightthickness=5)
            canvas4.place(x=root.winfo_screenwidth() - 270, y=50)
            link1 = Label(canvas4,font=('Verdana', 12), text="Login", fg="blue", bg="white", cursor="hand2")
            link1.place(x=120, y=50)
            link1.bind("<Button-1>", lambda e: loginPage())

        elif login == 1:

            if canvas4 is not None:
                canvas4.config(height=0, width=0)
                canvas4.delete("all")
            canvas4 = Canvas(root, bg="white", width=230, height=100,
                             highlightthickness=0)  # highlightbackground="black",highlightthickness=5)
            canvas4.place(x=root.winfo_screenwidth() - 270, y=50)
            canvas4.create_text(80, 25, fill="black", font="Times 14 bold", text="Login : ")
            canvas4.create_text(140, 25, fill="blue", font="Times 14 bold ", text="hello")
            image6 = Image.open("Pictures/signout.png")
            image6 = image6.resize((30, 30), Image.ANTIALIAS)
            photo_image6 = ImageTk.PhotoImage(image6)
            button1 = HoverButton(canvas4, compound=TOP, bg="black", image=photo_image6, borderwidth=0,
                                  command=lambda: loginPage(),activebackground='blue', cursor="hand2")
            button1.place(x=120, y=50)

            # image7 = Image.open("Pictures/homeicon.jpg")
            # image7 = image7.resize((30, 30), Image.ANTIALIAS)
            # photo_image7 = ImageTk.PhotoImage(image7)
            # button2 = HoverButton(canvas4, compound=TOP, fg="white", bg="black", image=photo_image7, borderwidth=0, activebackground='blue', cursor="hand2")#command=lambda: homemiddlepart(username.get()),
            # button2.place(x=60, y=50)
    except:
        log_except()

def loginPage():
    try:
        global canvas5, username, reportGameGraph, password, entry1, entry2, font_size, canvas1, login, back, canvas2, photo_image9, roll, numberChoosen1, canvas2, photo_image2, photo_image3

        back.append(5)
        if canvas1 is not None:
            canvas1.config(height=0, width=0)
            canvas1.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        if canvas2 is not None:
            canvas2.config(height=0, width=0)
            canvas2.delete("all")
        if canvas is not None:
            canvas.destroy()
        if entry3 is not None:
            entry3.destroy()

        login = 0
        username = StringVar()
        password = StringVar()
        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="Login")
        canvas2 = Canvas(root, bg="white", width=root.winfo_screenwidth() - 40, height=root.winfo_screenheight() - 165,
                         highlightbackground="blue", highlightthickness=20)
        canvas2.place(x=0, y=30)

        # Images
        # photo_image2 = ImageTk.PhotoImage(image2)
        # canvas2.create_image(150, 100, image=photo_image2)
        photo_image3 = ImageTk.PhotoImage(image3)
        canvas2.create_image(150, 100, image=photo_image3)
        canvas5 = Canvas(root, bg="white", width=550, height=350, bd=0, relief='ridge',
                         highlightthickness=0)  # , highlightbackground="black", highlightthickness=5)
        canvas5.place(x=400, y=210)  # int(root.winfo_screenheight()/2)),
        canvas5.create_text(310, 40, fill="black", font="Times 25 italic bold", text="SHES Member Login")
        canvas5.create_text(150, 120, fill="black", font="Times 20 italic bold", text="User ID    : ")
        canvas5.create_text(150, 190, fill="black", font="Times 20 italic bold", text="Password : ")

        entry1 = Entry(canvas5, textvariable=username, bd=3, width=20, font=font_size)
        entry1.place(x=250, y=110)
        entry1.focus()
        entry1.delete(0, END)

        entry2 = Entry(canvas5, show="*", textvariable=password, bd=3, width=20, font=font_size)
        entry2.place(x=250, y=180)
        entry2.delete(0, END)

        button1 = HoverButton(canvas5, text="Login", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                              width=15, activebackground='blue',command=checkLogIn, cursor="hand2")# command=checkLogIn,
        button1.place(x=250, y=250)

        # canvas5.create_text(410, 300, fill="black", font="Times 10 italic bold", text="New user? Create an account. ")
        if db._userCount():
            link1=Label(canvas5,text="New user? Create an account. ",fg="blue",bg="white",cursor="hand2")
            link1.place(x=250,y=300)
            link1.bind("<Button-1>",lambda e:registration())
        canvas3 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas3.place(x=0, y=root.winfo_screenheight() - 95)
        canvas3.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 10 italic bold",
                            text="2019 © Seaferers Health Expert System")

        # button2 = HoverButton(canvas5, text="Register", bg="#007ED9", fg="white", font=('Helvetica', '15'),
        #                       command=lambda:registration(), width=15, activebackground='blue', cursor="hand2")
        # button2.place(x=320, y=250)

        # toprightmostpart()
    except:
        log_except()
def checkLogIn() :
    global username, password, login,entry3,entry4

    username=actNum = entry1.get()
    pinNum = entry2.get()

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
        canvas2.create_image(150, 100, image=photo_image3)
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

        # canvas5.create_text(460, 100, fill="black", font="Times 20 italic bold", text="Doctor Request")
        canvas5.create_text(600, 100, fill="black", font="Times 20 italic bold", text="Registration")
        #
        # doctor_img = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=report_image,
        #                       borderwidth=0,  cursor="hand2",activebackground="white",command=lambda: records(canvas5))#command=records,
        # doctor_img.place(x=370, y=140)
        report_img = HoverButton(canvas5, compound=TOP, width=170, height=170, bg="white", image=doctor_image,
                              borderwidth=0, cursor="hand2",activebackground="white",command=patientRegistration)  # command=lambda:runreport()
        report_img.place(x=520, y=140)  # x=790, y=140
        # ========================
    except:
        log_except()

def patientRegistration():
    try:

        global canvas5,canvas2, canvas4,canvas1, back,ship_entry,\
            cap_phone_entry,ship_email_entry, ship_email_pwd_entry,login_pwd_entry,label_msg,login
        back.append(3)
        # if canvas1 is not None:
        #     canvas1.config(height=0, width=0)
        #     canvas1.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        # if canvas2 is not None:
        #     canvas2.config(height=0, width=0)
        #     canvas2.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if canvas is not None:
            canvas.destroy()

        # if canvas5 is not None:
        #     canvas5.destroy()
        patient_name = StringVar()
        pat_phone = StringVar()
        pat_age = StringVar()
        pat_gender = StringVar()

        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="SHES Registration Form")



        canvas5 = Canvas(root, width=1000, height=500,bg="white", bd=0, relief='ridge',highlightthickness=0)

        canvas5.place(x=300, y=100)

        label_msg = Label(canvas5, font="Times 13", text="", bg="white",fg="blue", width=50)
        label_msg.place(x=180, y=35)
        canvas5.create_text(180, 80, fill="black", font=reg_text_size, text="Patient Name*           : ")
        canvas5.create_text(180, 160, fill="black", font=reg_text_size, text="Phone            : ")
        canvas5.create_text(180, 240, fill="black", font=reg_text_size, text="Age            : ")
        canvas5.create_text(180, 300, fill="black", font=reg_text_size, text="Gender      : ")
        pat_entry = Entry(canvas5, textvariable=patient_name, bd=3, width=11, font=font_size, validate="key")
        pat_entry.place(x=360, y=70)
        pat_phone_entry = Entry(canvas5, textvariable=pat_phone, bd=3, width=11, font=font_size, validate="key")
        pat_phone_entry.place(x=360, y=140)
        pat_age_entry = Entry(canvas5, textvariable=pat_age, bd=3, width=11, font=font_size, validate="key")
        pat_age_entry.place(x=360, y=210)
        pat_gender_entry = Entry(canvas5,show="*", textvariable=pat_gender, bd=3, width=11, font=font_size,
                                     validate="key")
        pat_gender_entry.place(x=360, y=280)

        save_button = HoverButton(canvas5, text="Save", bg="#007ED9", fg="white", font=('Helvetica', '15'),
                                  width=15, activebackground='blue', cursor="hand2") #, command=lambda: saveDetails()
        save_button.place(x=180, y=420)

        back_button = HoverButton(canvas6, image=photo_image9, width=90, height=backButton_height, bg="white",
                                  borderwidth=0,
                                  font=('Helvetica', '15'), command=backpage, cursor="hand2")
        back_button.place(x=50, y=580)

    except:
        log_except()

def registration():
    try:

        global canvas5,canvas2, canvas4,canvas1, back,ship_entry,\
            cap_phone_entry,ship_email_entry, ship_email_pwd_entry,login_pwd_entry,label_msg,login
        back.append(3)
        # if canvas1 is not None:
        #     canvas1.config(height=0, width=0)
        #     canvas1.delete("all")
        if canvas5 is not None:
            canvas5.config(height=0, width=0)
            canvas5.delete("all")
        # if canvas2 is not None:
        #     canvas2.config(height=0, width=0)
        #     canvas2.delete("all")
        if canvas4 is not None:
            canvas4.config(height=0, width=0)
            canvas4.delete("all")
        if canvas is not None:
            canvas.destroy()

        # if canvas5 is not None:
        #     canvas5.destroy()
        login = 2
        ship_name = StringVar()
        cap_phone = StringVar()
        ship_email = StringVar()
        ship_email_pwd = StringVar()
        login_pwd = StringVar()

        canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
                         highlightthickness=5)
        canvas1.place(x=0, y=0)
        canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text="SHES Registration Form")



        canvas5 = Canvas(root, width=1000, height=500,bg="white", bd=0, relief='ridge',highlightthickness=0)

        canvas5.place(x=300, y=100)

        label_msg = Label(canvas5, font="Times 13", text="", bg="white",fg="blue", width=50)
        label_msg.place(x=180, y=35)
        canvas5.create_text(180, 80, fill="black", font=reg_text_size, text="Ship Name*           : ")
        canvas5.create_text(180, 160, fill="black", font=reg_text_size, text="Phone            : ")
        canvas5.create_text(180, 240, fill="black", font=reg_text_size, text="Email ID*            : ")
        canvas5.create_text(180, 300, fill="black", font=reg_text_size, text="Email Password*      : ")
        canvas5.create_text(180, 380, fill="black", font=reg_text_size, text="Login Password*      : ")

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

        toprightmostpart()
    except:
        log_except()

# setting up the user details to a table
class records():
       # class created to see records that have been previously inputted#
    def __init__(self, root):
        self.master = root
        # self.master.geometry('250x200+100+200')
        # self.master.title('Records')
        self.connection = sqlite3.connect(json_const['DB_NAME'])
        self.cur = self.connection.cursor()
        self.dateLabel = Label(self.master, text="Date", width=10)
        self.dateLabel.grid(row=0, column=0)
        self.BMILabel = Label(self.master, text="BMI", width=10)
        self.BMILabel.grid(row=0, column=1)
        self.stateLabel = Label(self.master, text="Status", width=10)
        self.stateLabel.grid(row=0, column=2)
        self.stateLabel = Label(self.master, text="Status1", width=10)
        self.stateLabel.grid(row=0, column=3)
        self.stateLabel = Label(self.master, text="Status2", width=10)
        self.stateLabel.grid(row=0, column=4)
        self.stateLabel = Label(self.master, text="Status3", width=10)
        self.stateLabel.grid(row=0, column=5)
        self.showallrecords()

    def showallrecords(self):
        data = self.readfromdatabase()
        for index, dat in enumerate(data):
            Label(self.master, text=dat[0]).grid(row=index + 1, column=0)
            Label(self.master, text=dat[1]).grid(row=index + 1, column=1)
            Label(self.master, text=dat[2]).grid(row=index + 1, column=2)
            Label(self.master, text=dat[3]).grid(row=index + 1, column=3)
            Label(self.master, text=dat[4]).grid(row=index + 1, column=4)
            Label(self.master, text=dat[5]).grid(row=index + 1, column=5)

    def readfromdatabase(self):
        self.cur.execute("SELECT * FROM user_reg")
        return self.cur.fetchall()
# table ended
def saveDetails():
    # print("in save method")
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

def on_closing():
    try:
        logging.info("On closing ")
        d = dialoguebox(root, text="Do you want to exit the application?", buttons=["Yes", "No"], default=0,
                        cancel=2, title=warn, icon='Pictures/warn.png')
        if (d.go()) == 0:

            force_kill()
    except:
        log_except()
with open('Const/config.json') as i:
    json_const = json.load(i)
envMode = json_const["ENVIRONMENT"]
def force_kill():
    try:
        logging.info("In force kill... ")
        if envMode == "development":
            os.system("taskkill /f /im database_Server.py 1>nul")
            os._exit(0)
        else:
            if (platform.system()=="Windows"):

                os.system("taskkill /f /im database_Server.exe 1>nul 2>nul")
                os._exit(0)
            else:
                os.system("sudo pkill database_Server")
                os._exit(0)
    except:
        log_except()

loginPage()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
if (platform.system()=="Linux"):
    root.attributes('-zoomed', True)
else:
    root.state('zoomed')

root.protocol("WM_DELETE_WINDOW", on_closing)
img = PhotoImage(file='Pictures/icon2.png')
root.tk.call('wm', 'iconphoto', root._w, img)

root.mainloop()