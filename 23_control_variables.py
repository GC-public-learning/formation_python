#coding:utf-8

""" control variables
------------------------"""

from tkinter import *

main_app = Tk()
main_app.title("My window")
main_app.geometry("800x600")

"""
Kinds of variables
-----------------------
StringVar()
IntVar()
DoubleVar()
BooleanVar()
"""

""" variables
--------------"""
var_label_1 = StringVar()
var_entry_1 = StringVar()
var_radiobtn = IntVar()


""" assigniations
------------------------"""
var_label_1.set("Hello")


""" create
--------------"""
label_1 = Label(main_app, width=20, textvariable=var_label_1)
entry_1 = Entry(main_app, textvariable=var_entry_1) 
radiobtn_1 = Radiobutton(main_app, text="radio1", 
	value=0, variable=var_radiobtn)
radiobtn_2 = Radiobutton(main_app, text="radio2", 
	value=1, variable=var_radiobtn)
radiobtn_3 = Radiobutton(main_app, text="radio3", 
	value=2, variable=var_radiobtn)

""" use
-----------"""
entry_1.pack()
label_1.pack()
radiobtn_1.pack()
radiobtn_2.pack()
radiobtn_3.pack()




""" traceability
------------------------"""

# functions triggered by traced variables
def update_label_1(*args):
	var_label_1.set(var_entry_1.get()) 

def print_state_radiobutton(*args):
	print(var_radiobtn.get())


# traced variables
# and execute function when action on them:
# possible actions : r(read), w(write), u(undefine)
var_entry_1.trace('w', update_label_1)
var_radiobtn.trace('w', print_state_radiobutton)



main_app.mainloop()
