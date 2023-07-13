from tkinter import * 

window = Tk()
window.config()

label_1 = Label(text="LABEL 1", bg="#F00")
label_1.grid(row=0, column=0, rowspan=3)
label_2 = Label(text="LABEL 2", bg="#0F0")
label_2.grid(row=1, column=1)

window.mainloop()