#coding:utf-8

""" tkinter widget positioning
---------------------------------"""

from tkinter import *

# window 1
main_app = Tk()
main_app.title("My window")
main_app.geometry("800x600+50+200")

# window 2
app = Tk()
app.title("2nd window")
app.geometry("800x600-50+200")


""" create
--------------"""

# window 1

# frame
mainframe = Frame(main_app, width=800, height=200)

# labelframe
labelframe_1 = LabelFrame(mainframe, text="label frame",
	width=800, height=200, borderwidth=1)

btn_1 = Button(main_app, text="Start")
label_1 = Label(main_app, text="label 1")
entry_1 = Entry(labelframe_1)


# window 2
btn_2 = Button(app, text="Start")
label_2 = Label(app, text="label 1")
entry_2 = Entry(app)


""" use
-----------"""

# window 1 (pack)

# side : left, right, top, bottom
mainframe.pack(side="top") # default position
labelframe_1.pack()
entry_1.pack()

# padx and pady : extern margin, ipadx and ipady : intern margin
label_1.pack(padx=20, pady=20, ipady=20, ipadx=20)

# expand (extends the space around the widget over the remaining space)
# fill (extends the widget on its space) possible values : 'x', 'y', "both"
btn_1.pack(expand=True, fill="both")




# window 2 (grid) default position x=0, y=0
entry_2.grid(row=0, column=0, pady=20, padx=20)
label_2.grid(row=1, column=1)

# span : extand over several squares
# sticky : place de widget in its space in such position : n,s,w,e
btn_2.grid(row=3, column=0, rowspan=2, columnspan=3, sticky="se")


""" place 
---------------
instead of use "pack" or "grid" you can also use "place" 
ex : element.place(x=10, y=10) relx, rely for relative positions


"""



main_app.mainloop()
app.mainloop()
