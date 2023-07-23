from tkinter import *
from tkinter import messagebox
from datetime import date

def add_film():

    movie_rating = rating_entry.get()
    rating_entry.delete(0, len(movie_rating))

    try:
        movie_rating = int(movie_rating)
    except:
        messagebox.showinfo(title="Ooops", message="enter number from -5 to 5")

    movie_name = name_entry.get()
    name_entry.delete(0, len(movie_name))

    if len(movie_name) > 0 and movie_rating <= 5 and movie_rating >= -5:    
        with open("movie_data.txt", mode="r+") as movie_data:
            movie_number = int(movie_data.readlines()[-1][0]) + 1
            movie_data.write(f"{movie_number}. {date.today()} | {movie_name} | {movie_rating}\n")

    else:
        messagebox.showinfo(title="Oooops", message="Enter movie name and movie rating between -5 and 5")


CANVAS_HEIGHT = 200
CANVAS_WIDTH = 200
FONT_STYLE = "Courier"

FONT = (FONT_STYLE, 14, NORMAL)

window = Tk()
window.config(padx=50, pady=50)

img = PhotoImage(file="movie.png")
logo = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
logo.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=img)
logo.grid(row=0, column=0, columnspan=3, pady=30)

name_label = Label(text="Movie name: ", pady=10, font=FONT)
name_label.grid(row=1, column=0, sticky="w")
name_entry = Entry()
name_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

rating_label = Label(text="Movie rating: ", font=FONT)
rating_label.grid(row=2, column=0, sticky="w")
rating_entry = Entry()
rating_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

button = Button(text="Add film", font=FONT, fg="red", command=add_film)
button.grid(row=3, column=0, columnspan=3, sticky="ew", pady=5)

window.mainloop()