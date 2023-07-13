from tkinter import *

def calculate_km():
    miles = int(miles_num.get())
    km_num["text"] = str(int(miles*1.6))

window = Tk()
window.config(padx=20, pady=20)
window.minsize(width=200, height=100)

equal_label = Label(text="is equal to", pady=10)
equal_label.grid(column=0, row=1)

miles_num = Entry(width=10)
miles_num.grid(column=1, row=0)
miles_label = Label(text="Miles", padx=20)
miles_label.grid(column=2, row=0)

km_num = Label(text="0")
km_num.grid(row=1, column=1)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(row=2, column=1)

window.mainloop()