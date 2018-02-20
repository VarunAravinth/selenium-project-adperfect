from Tkinter import *
import Tkinter as ttk
from ttk import *
import Tkinter as tk
import random
from tkMessageBox import askokcancel           

#window = Tk()
window = tk.Tk()
window.configure(background='')
 
window.title("Welcome to LikeGeeks app")
window.geometry('640x650+0+0')

 
lbl = Label(window, text="Title")
lbl.grid(column=0,row=0, padx=2, pady=2)
txt1 = Entry(window,width=23)
txt1.grid(column=1,row=0,  padx=2, pady=2)

lbl = Label(window, text="Description")
lbl.grid(column=0, row=1, padx=2, pady=2)
text_box = Text(window, height=6, width=17)
text_box.grid(column=1, row=1, padx=2, pady=2)

lbl = Label(window, text="Residential/Commercial")
lbl.grid(column=0, row=3, padx=2, pady=2)
combo = Combobox(window)
combo['values']= ("-select-","Residential", "Commercial", "Residential & Commercial")
combo.current(1) #set the selected item
combo.grid(column=1, row=3, padx=2, pady=2)

lbl = Label(window, text="Choose a category")
lbl.grid(column=0, row=4, padx=2, pady=2)
combo = Combobox(window)
combo['values']= ("-select-","Licensed", "Insured", "Licensed & Insured")
combo.current(1) #set the selected item
combo.grid(column=1, row=4, padx=2, pady=2)

chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Free Estimates', var=chk_state)
chk.grid(column=1, row=5, padx=2, pady=2)

lbl = Label(window, text="Website")
lbl.grid(column=0, row=6, padx=2, pady=2)
txt = Entry(window,width=23)
txt.grid(column=1, row=6, padx=2, pady=2)

lbl = Label(window, text="Price")
lbl.grid(column=0, row=7, padx=2, pady=2)
txt = Entry(window,width=23)
txt.grid(column=1, row=7, padx=2, pady=2)

 
rad1 = Radiobutton(window,text='Phone Number', value=1)
rad1.grid(column=1, row=8, padx=2, pady=2)

rad2 = Radiobutton(window,text='E-mail', value=2)
rad2.grid(column=1, row=9, padx=2, pady=2)

rad3 = Radiobutton(window,text='Both', value=3)
rad3.grid(column=1, row=10, padx=2, pady=2)

lbl = Label(window, text="Phone Number")
lbl.grid(column=0, row=11, padx=2, pady=2)
txt = Entry(window,width=23)
txt.grid(column=1, row=11)

lbl = Label(window, text="E-mail")
lbl.grid(column=0, row=12, padx=2, pady=2)
txt = Entry(window,width=23)
txt.grid(column=1, row=12, padx=2, pady=2)

lbl = Label(window, text="Address")
lbl.grid(column=0, row=13, padx=2, pady=2)
txt = Entry(window,width=23)
txt.grid(column=1, row=13, padx=2, pady=2)

lbl = Label(window, text="City")
lbl.grid(column=0, row=14, padx=2, pady=2)
txt = Entry(window,width=23)
txt.grid(column=1, row=14, padx=2, pady=2)

lbl = Label(window, text="Postal Code")
lbl.grid(column=0, row=15, padx=2, pady=2)
txt = Entry(window,width=23)
txt.grid(column=1, row=15, padx=2, pady=2)

lbl = Label(window, text="Online Title")
lbl.grid(column=0, row=16, padx=2, pady=2)
txt = Entry(window,width=23)
txt.grid(column=1, row=16, padx=2, pady=2)

lbl = Label(window, text="Online Ad Copy")
lbl.grid(column=0, row=17, padx=2, pady=2)
text_box = Text(window, height=6, width=17)
text_box.grid(column=1, row=17, padx=2, pady=2)


lbl = Label(window, text="Dates")
lbl.grid(column=0, row=18, padx=2, pady=2)
txt = Entry(window,width=23)
txt.grid(column=1, row=18, padx=2, pady=2)

def submit():
    print txt1.get()
    #print text_box1.get()

tk.Button(window,text="submit",command=submit).grid()


window.mainloop()
