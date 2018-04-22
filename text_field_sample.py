from Tkinter import *
import Tkinter as ttk
from ttk import *
 
root = Tk()
root.title("First Website")

 
# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

def change_dropdown3(*args):
    #print('New change')
    global argg3
    argg3 = tkvar3.get()
    print(argg3) 
# Create a Tkinter variable
tkvar3 = StringVar(root)
argg3=''

Label(mainframe,text='Title').grid(row=5,column=1)
Entry(mainframe,width=23,textvariable = tkvar3).grid(row=5,column=2)

    
    
 
# link function to change dropdown
tkvar3.trace('w', change_dropdown3)


root.mainloop()
