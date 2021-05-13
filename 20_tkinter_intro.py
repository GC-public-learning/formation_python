#coding:utf-8

""" tkinter intro
----------------------"""

""" list of other libraries GUI (Graphic User Interface) :
	site : https://docs.python.org/3/faq/gui.html """

from tkinter import * # (native library)

# make a window (tkinter object)
main_app = Tk()

# title
main_app.title("My Window")

# size & position
main_app.geometry("800x600+50+50")
main_app.minsize(648, 480)
main_app.maxsize(1024, 768)
# main_app.sizefrom("user")
# main_app.positionfrom("user")

# center
screen_x = main_app.winfo_screenwidth()
screen_y = main_app.winfo_screenheight()
window_x = 800
window_y = 600

position_x = (screen_x // 2) - (window_x // 2) # // : get a int
position_y = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x, window_y, position_x, position_y)

main_app.geometry(geo)

# allow or forbid resizing on width an height
main_app.resizable(width = False, height = True)


# make a infinite loop on the window
main_app.mainloop()

#quit the window manually
# main_app.quit()
