#coding:utf-8

""" menu
------------------------"""

from tkinter import *

main_app = Tk()
main_app.title("My window")
main_app.geometry("800x600")


""" called functions
----------------------"""
def say_hello():
	print("hello ! ")

# TopLevel: create a sub window
def show_secret_window():
	secret_window = Toplevel(main_app)
	secret_window.title("Secret Window")


""" create
--------------"""
menu_0 = Menu(main_app)

# tearoff : remove the default separator
menu_0_0 = Menu(menu_0, tearoff=False)
menu_0.add_cascade(label="menu 0", menu=menu_0_0)
menu_0_0.add_command(label="option 1")
menu_0_0.add_command(label="option 2")
menu_0_0.add_command(label="option 3")

menu_0_1 = Menu(menu_0)
menu_0.add_cascade(label="menu 1", menu=menu_0_1)
menu_0_1.add_command(label="option 1")
menu_0_1.add_command(label="option 2")
menu_0_1.add_command(label="option 3")

menu_0_0_0 = Menu(menu_0_0)
menu_0_0.add_cascade(label="menu 0.0", menu=menu_0_0_0)
menu_0_0_0.add_command(label="secret", command=show_secret_window)
menu_0_0_0.add_command(label="say hello !", command=say_hello)
menu_0_0_0.add_command(label="quit", command=main_app.quit)

menu_0_1_0 = Menu(menu_0_1)
menu_0_1.add_cascade(label="menu 0.1", menu=menu_0_1_0)
#other possible addings
menu_0_1_0.add_checkbutton()
menu_0_1_0.add_separator()
menu_0_1_0.add_radiobutton()




""" use
-----------"""
main_app.config(menu=menu_0)



main_app.mainloop()
