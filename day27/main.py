from tkinter import *

window = Tk()

label = Label(text="Hello world")
label.grid(column=0, row=0)

button1 = Button(text="Button")
button1.grid(column=1, row=1)

button2 = Button(text="New Button", bg="blue")
button2.grid(column=2, row=0)

input = Entry(text="Entry")
input.grid(column=3, row=2)

window.mainloop()