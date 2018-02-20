from Tkinter import *
import Tkinter as ttk
from ttk import *
import Tkinter as tk
import random
from tkMessageBox import askokcancel           

fields = 'Title', 'Description', 'Residential','Licene', 'Websit', 'Price','Phone number','Email','Address', 'City', 'Postal Code', 'Online Title', 'Online Ad Copy','Date'

def fetch(entries):
    for entry in entries:
        print 'Input => "%s"' % entry.get()

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)                  
        lab = Label(row, width=20, text=field)
        ent = Entry(row)
        row.pack(side=TOP, fill=Y)           
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=Y)
        entries.append(ent)
    return entries

def show(entries):
    fetch(entries)
    popup.destroy()

def ask():
    global popup
    popup = Toplevel()
    ents = makeform(popup, fields)
    Button(popup, text='OK', command=(lambda e=ents: show(e)) ).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()

root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()
