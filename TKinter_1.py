from tkinter import *
from tkinter.ttk import *


# We First need to create a main window
# to put Widgets in in.
# By the way Widgets are the elements of the GUI application
# Which provides various controls to users to interact with
# the application.


# Some of the widgets in tkinter are radiobutton, checkbox, labels etc.


# Creating root window.

root = Tk()

# Giving title to the main window!!

root.title('First Program.')

# Label is what output will be
# Show on the window.
label = Label(root, text = "Hello World!").pack()



# calling mainloop method which is used
# when your application is ready to run
# and it tells the code to keep displaying

root.mainloop()