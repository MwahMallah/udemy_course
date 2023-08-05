from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json

CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200

def search_website():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        password = data[website]["password"]
        email = data[website]["email"]
    except (FileNotFoundError, KeyError):
        messagebox.showinfo(title="Error", message="No details for website exists")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.insert(0, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = website_entry.get()
    website_entry.delete(0, len(website))
    email = email_entry.get()
    password = password_entry.get()
    password_entry.delete(0, len(password))

    new_entry = {
        website : {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Ooops", message="Don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_entry, data_file, indent=4)

        else:
            data.update(new_entry)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

                    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

lock_logo = Canvas(master=window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
lock_img = PhotoImage(file="logo.png")
lock_logo.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=lock_img)
lock_logo.grid(row=0, column=1)

website_label = Label(master=window, text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=1, sticky="w")
website_entry.focus()

search_button = Button(text="Search", command=search_website)
search_button.grid(column=2, row=1, sticky="ew")

email_label = Label(master=window, text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky="ew")
email_entry.insert(0, "maximus27rus@gmail.com")

password_label = Label(master=window, text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="w")
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky="e")

add_button = Button(text="Add", command=add_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
