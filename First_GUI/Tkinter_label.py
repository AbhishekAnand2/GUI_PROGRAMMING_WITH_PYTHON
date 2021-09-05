from tkinter import *

root = Tk()

# Geometry function takes arguments as "WIDTH X HEIGHT"
# Geometry is a Kickstart function for every GUI
root.geometry("444x444")

# fixing minimum size of the GUI window
# Arguments that our minsize and maxsize function will take is in format of
# "Width x Height"
root.minsize(200,100) # this prohibits the GUI to resize till 0

# Maxsize function

root.maxsize(999,1080)

# Label is a thing with which user isn't interact with.

label = Label(text="Abhishek is a Good Boy!")
# This label won't print as we need to pack GUI to be shown over GUI window.
# So we cam use pack function to pack GUI

label.pack()

root.mainloop()