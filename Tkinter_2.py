from tkinter import *


# creating a root window
root = Tk()
# frame inside a root window.
frame = Frame(root)

# geometry method : This method is a fundamental one which decides the
# size, position and some other attributes of the Screen Layout which we
# aregoing to create.
frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

redbutton = Button(frame, text="Red", fg="green") # this sets button inside frame with text
# written as "Red" but color of the text will be green as fg sets color as green
redbutton.pack(side=LEFT)

redButton = Button(frame,text="hey!",fg="red")
redButton.pack(side=LEFT)

Blue_Button = Button(frame,text="hey!",fg="Blue")
Blue_Button.pack(side=LEFT)

black_button = Button(bottom_frame,text="Heyaaa!!",fg="black")
black_button.pack(side=BOTTOM)
root.mainloop()


