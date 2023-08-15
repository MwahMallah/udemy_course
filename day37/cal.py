from tkinter import *
from tkcalendar import *
import requests

TOKEN = "kajsfdhasdjkfhdsafj"
USERNAME = "mwahmallah"
GRAPH = "graph1"
PIXELA = "https://pixe.la/v1/users"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

def delete_pixel():
    headers = HEADERS 
    url_endpoint = f"{PIXELA}/{USERNAME}/graphs/{GRAPH}/{get_date()}"
    response = requests.delete(url=url_endpoint, headers=headers)
    print(response)


def add_pixel():
    url_endpoint = f"{PIXELA}/{USERNAME}/graphs/{GRAPH}/{get_date()}"

    headers = HEADERS

    params = {
        "quantity": get_hours()
    }

    response = requests.put(url=url_endpoint, json=params, headers=headers)
    print(response)

def get_date(): 
    return calendar.get_date()

def get_hours(): 
    return enter_hours_input.get()


BG = "#204985"
FONT = ("Helvetica", 12, "normal")

window = Tk()
window.config(width=300, height=300, pady=20, padx=30)
calendar = Calendar(window, date_pattern="yyyyMMdd")
calendar.grid(row=0, column=0, columnspan=2, pady=20)

enter_hours_label = Label(text="Enter num of hours: ", bg=BG, fg="white", font=FONT)
enter_hours_label.grid(row=1, column=0, sticky="ew")

enter_hours_input = Entry(font=FONT, bg=BG, fg='white')
enter_hours_input.grid(row=1, column=1, sticky="ew", padx=10)

add_button = Button(text="Add", font=FONT, bg=BG, fg='white', highlightthickness=0, relief='flat', bd=0, command=add_pixel)
add_button.grid(row=2, column=0, sticky="ew", pady=10)

delete_button = Button(text="Delete", font=FONT, bg=BG, fg='white', highlightthickness=0, relief='flat', bd=0, command=delete_pixel)
delete_button.grid(row=2, column=1, sticky="ew", pady=10, padx=10)

window.mainloop()