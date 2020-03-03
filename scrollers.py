import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
import platform
import time
import os
import mysql.connector
import logging
import json
from PIL import Image, ImageTk
import database_Server as db
import commonFunction
# import table
# from table_display import demo
from utilities import write_log_file,log_except
with open('Const/config.json') as i:
    json_const = json.load(i)

#
# import tkinter as tk
#
# root=tk.Tk()
#
# vscrollbar = tk.Scrollbar(root)
#
# c= tk.Canvas(root,background = "#D2D2D2",yscrollcommand=vscrollbar.set)
#
# vscrollbar.config(command=c.yview)
# vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#
# f=tk.Frame(c) #Create the frame which will hold the widgets
#
# c.pack(side="RIGHT", fill="both", expand=True)
#
# #Updated the window creation
# c.create_window(0,0,window=f, anchor='nw')
#
# #Added more content here to activate the scroll
# for i in range(100):
#     tk.Label(f,wraplength=350 ,text=r"Det er en kendsgerning, at man bliver distraheret af læsbart indhold på en side, når man betragter dens websider, som stadig er på udviklingsstadiet. Der har været et utal af websider, som stadig er på udviklingsstadiet. Der har været et utal af variationer, som er opstået enten på grund af fejl og andre gange med vilje (som blandt andet et resultat af humor).").pack()
#     tk.Button(f,text="anytext").pack()
#
# #Removed the frame packing
# #f.pack()
#
# #Updated the screen before calculating the scrollregion
# root.update()
# c.config(scrollregion=c.bbox("all"))
#
# root.mainloop()
import tkinter as tk
root = tk.Tk()
root.title('Admin - Seaferers Health Expert System')
LABEL_BG = "white"  # Light gray.
ROWS, COLS = 10, 6  # Size of grid.
ROWS_DISP = 10  # Number of rows to display.
COLS_DISP = 6  # Number of columns to display.

def MyApp():

        master = Canvas(root, bg="white", width=600, height=350, bd=0, relief='ridge', highlightthickness=10)
        master.place(x=270, y=210)
        # Create a frame for the canvas and scrollbar(s).
        frame2 = tk.Frame(master)
        frame2.grid(row=3, column=3, sticky=tk.NW)
               # Add a canvas in that frame.
        canvas = tk.Canvas(frame2, bg="Yellow")
        canvas.grid(row=0, column=0)

        # Create a vertical scrollbar linked to the canvas.
        vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.grid(row=0, column=1, sticky=tk.NS)
        canvas.configure(yscrollcommand=vsbar.set)

        # Create a horizontal scrollbar linked to the canvas.
        # hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
        # hsbar.grid(row=1, column=0, sticky=tk.EW)
        # canvas.configure(xscrollcommand=hsbar.set)

        # Create a frame on the canvas to contain the buttons.
        shipdetails_frame = tk.Frame(canvas, bg="Black", bd=2)

        # Add the buttons to the frame.
        showallrecords(shipdetails_frame)
        # Create canvas window to hold the shipdetails_frame.
        canvas.create_window((0,0), window=shipdetails_frame, anchor=tk.NW)

        shipdetails_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
        print('canvas.bbox(tk.ALL): {}'.format(bbox))

        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        print(ROWS)

        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        print(h)
        dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
        canvas.configure(scrollregion=bbox, width=dw, height=dh)
        #
        # label3 = tk.Label(root, text="Frame3 Contents", bg=LABEL_BG)
        # label3.grid(row=4, column=0, pady=5, sticky=tk.NW)
        #
        # frame3 = tk.Frame(master, bg="Blue", bd=2, relief=tk.GROOVE)
        # frame3.grid(row=5, column=0, sticky=tk.NW)

def showallrecords(master):
    data = readfromdatabase()
    dateLabel = Label(master, text="S.No", width=10, height=3, relief="ridge", bg="black", fg="white")
    dateLabel.grid(row=0, column=0)
    dateLabel = Label(master, text="Ship Name", width=20, height=3, relief="ridge", bg="black",
                      fg="white")
    dateLabel.grid(row=0, column=1)
    BMILabel = Label(master, text="Ship Email Id", width=40, height=3, relief="ridge", bg="black",
                     fg="white")
    BMILabel.grid(row=0, column=2)
    stateLabel = Label(master, text="Starting Location", width=20, height=3, relief="ridge", bg="black",
                       fg="white")
    stateLabel.grid(row=0, column=3)
    stateLabel = Label(master, text="Ending Location", width=20, height=3, relief="ridge", bg="black",
                       fg="white")
    stateLabel.grid(row=0, column=4)
    for index, dat in enumerate(data):
            tk.Label(master, text=index+1,relief="ridge",width=10,bg="white",height=2).grid(row=index + 1, column=0)
            tk.Label(master, text=dat[0],relief="ridge",width=20,bg="white",height=2).grid(row=index + 1, column=1)
            tk.Label(master, text=dat[1],relief="ridge",width=40,bg="white",height=2).grid(row=index + 1, column=2)
            tk.Label(master, text=dat[2],relief="ridge",width=20,bg="white",height=2).grid(row=index + 1, column=3)
            tk.Label(master, text=dat[3],relief="ridge",width=20,bg="white",height=2).grid(row=index + 1, column=4)



def readfromdatabase():
    connection = mysql.connector.connect(host=json_const['Server'], user=json_const['db_Username'],
                                              passwd=json_const['DB_Password'],
                                              database=json_const['Database_name'])
    cur = connection.cursor()
    cur.execute("SELECT ship_name,ship_email,ship_start_point,ship_end_point FROM ship_registration")
    return cur.fetchall()

m=MyApp()

root.mainloop()
# from tkinter import *
#
#
# class ScrollableFrame(Frame):
#     def __init__(self, parent, minimal_canvas_size, *args, **kw):
#         '''
#         Constructor
#         '''
#
#         Frame.__init__(self, parent, *args, **kw)
#
#         self.minimal_canvas_size = minimal_canvas_size
#
#         # create a vertical scrollbar
#         vscrollbar = Scrollbar(self, orient = VERTICAL)
#         vscrollbar.pack(fill = Y, side = RIGHT, expand = FALSE)
#
#         # create a horizontal scrollbar
#         hscrollbar = Scrollbar(self, orient = HORIZONTAL)
#         hscrollbar.pack(fill = X, side = BOTTOM, expand = FALSE)
#
#         #Create a canvas object and associate the scrollbars with it
#         self.canvas = Canvas(self, bd = 0, highlightthickness = 0, yscrollcommand = vscrollbar.set, xscrollcommand = hscrollbar.set)
#         self.canvas.pack(side = LEFT, fill = BOTH, expand = TRUE)
#
#         #Associate scrollbars with canvas view
#         vscrollbar.config(command = self.canvas.yview)
#         hscrollbar.config(command = self.canvas.xview)
#
#
#         # set the view to 0,0 at initialization
#
#         self.canvas.xview_moveto(0)
#         self.canvas.yview_moveto(0)
#
#         self.canvas.config(scrollregion='0 0 %s %s' % self.minimal_canvas_size)
#
#         # create an interior frame to be created inside the canvas
#
#         self.interior = interior = Frame(self.canvas)
#         interior_id = self.canvas.create_window(0, 0, window=interior,
#                 anchor=NW)
#
#         # track changes to the canvas and frame width and sync them,
#         # also updating the scrollbar
#
#         def _configure_interior(event):
#             # update the scrollbars to match the size of the inner frame
#             size = (max(interior.winfo_reqwidth(), self.minimal_canvas_size[0]), max(interior.winfo_reqheight(), self.minimal_canvas_size[1]))
#             self.canvas.config(scrollregion='0 0 %s %s' % size)
#             if interior.winfo_reqwidth() != self.canvas.winfo_width():
#                 # update the canvas's width to fit the inner frame
#                 self.canvas.config(width = interior.winfo_reqwidth())
#         interior.bind('<Configure>', _configure_interior)
#
#
# class my_gui(Frame):
#
#     def __init__(self):
#         # main tk object
#         self.root = Tk()
#
#         # init Frame
#         Frame.__init__(self, self.root)
#
#         minimal_canvas_size = (500, 500)
#
#         # create frame (gray window)
#
#         self.frame = ScrollableFrame(self.root, minimal_canvas_size)
#         self.frame.pack(fill=BOTH, expand=YES)
#
#         self.__add_plot()
#
#     def __add_plot(self):
#         # create a rectangle
#         self.frame.canvas.create_polygon(10, 10, 10, 150, 200, 150, 200, 10,  fill="gray", outline="black")
#
#     def mainLoop(self):
#         # This function starts an endlos running thread through the gui
#         self.root.mainloop()
#
#     def __quit(self):
#         # close everything
#         self.root.quit()
#
#
# # init gui
# my_gui = my_gui()
# # execute gui
# my_gui.mainLoop()

