from tkinter import *

root = Tk()

root.geometry("720x720")
root.minsize(300,200)
root.maxsize(720,1080)

label = Label(text="Welcome to the Pycharm!")
label.pack()
label2 = Label(text = "PYCharm 2.3")
label2.pack()

root.mainloop()