from tkinter import *
master = Tk()
canvas = Canvas(master)
canvas.grid(row=0,column=0)
hbar = Scrollbar(master, orient=HORIZONTAL)
hbar.config(command=canvas.xview)
hbar.grid(row=1, column=0, sticky=E+W)
vbar = Scrollbar(master, orient=VERTICAL)
vbar.config(command=canvas.yview)
vbar.grid(row=0,column=1,sticky=N+S)

canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
master.mainloop()