#coding:utf-8

""" tkinter advanced widgets
------------------------------"""

from tkinter import *

main_app = Tk()

""" create
--------------"""

# check button
checkbtn_1 = Checkbutton(main_app, text = "Publish")

# radio button
radiobtn_1 = Radiobutton(main_app, text = "men", value = 1)
radiobtn_2 = Radiobutton(main_app, text = "woman", value = 0)

# scale
scale_w = Scale(main_app, from_ = 10, to = 100, tickinterval = 25)

# spinbox
spinbox_1 = Spinbox(main_app)

# listbox
listbox_1 = Listbox(main_app)
listbox_1.insert(1, "Windows")
listbox_1.insert(2, "Linux")
listbox_1.insert(2, "mACoS")

# messagebox (triggered by buttons here)
from tkinter import messagebox # mendatory !

def show_error():
	messagebox.showerror("Error !",  "there is a error")
def show_info():
	messagebox.showinfo("Info", "this is an info")
def show_warning():
	messagebox.showwarning("Warning", "this is a warning")
def ask_question():
	messagebox.askquestion("question", "yes or not ?")
def ask_okcancel():
	messagebox.askokcancel("question", "ok or cancel ?")
def ask_yesno():
	messagebox.askyesno("question", "yes or no ?")
def ask_retrycancel():
	messagebox.askokcancel("question", "ok or cancel ?")

btn_show_error = Button(main_app, text = "Show error", command = show_error)
btn_show_info = Button(main_app, text = "Show info", command = show_info)
btn_show_warning = Button(main_app, text = "Show warning", 
	command = show_warning)
btn_ask_quesiton = Button(main_app, text = "Show yes or not", 
	command = ask_question)
btn_ask_okcancel = Button(main_app, text = "Show ok or cancel", 
	command = ask_okcancel)
btn_ask_yesno = Button(main_app, text = "Show yes or no", 
	command = ask_yesno)
btn_ask_retrycancel = Button(main_app, text = "Show ok or cancel", 
	command = ask_retrycancel)




""" use
-----------"""
checkbtn_1.pack()
radiobtn_1.pack()
radiobtn_2.pack()
scale_w.pack()
spinbox_1.pack()
listbox_1.pack()
btn_show_error.pack()
btn_show_info.pack()
btn_show_warning.pack()
btn_ask_quesiton.pack()
btn_ask_okcancel.pack()
btn_ask_yesno.pack()
btn_ask_retrycancel.pack()



main_app.mainloop()
