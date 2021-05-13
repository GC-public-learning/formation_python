#coding:utf-8

""" 1st widgets
----------------------"""

from tkinter import *

main_app = Tk()

""" create
-------------"""
# label
lbl_welcome = Label(main_app, text = "welcome everybody ! ")

# message (several lines)
msg_welcome = Message(main_app, text = "welcome everybody ! ")

# text entry
entry_name = Entry(main_app)
entry_pwd = Entry(main_app, show = "*") # show : replace chars by *

# button
btn_quit = Button(main_app, text = "quit")

def say_hello():
	print("Hello !")

btn_say_hello = Button(main_app, text = "say Hello !", command = say_hello)


# common params
# width in px or not, height, command

""" use widgets (autocenter)
------------------------------------"""
lbl_welcome.pack()
msg_welcome.pack()
entry_name.pack()
entry_pwd.pack()
btn_quit.pack()
btn_say_hello.pack()

""" read params
-------------------"""
print(lbl_welcome.cget("text"))
print(lbl_welcome["text"])



""" config params
-------------------"""
lbl_welcome["text"] = "Hi !"
lbl_welcome.configure(text = "Hello !")
lbl_welcome.config(text = "How are you taoday ?") # alias






main_app.mainloop()