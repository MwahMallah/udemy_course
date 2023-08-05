from tkinter import *
from tkinter import messagebox
import pandas
import random

IMAGE_WIDTH = 800
IMAGE_HEIGHT = 526
TIME_UNTILL_FOLDING = 3000

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
SCORE_FONT = ("Ariel", 30, "normal")

try:
    df = pandas.read_csv("data/new_spanish_words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    df = pandas.read_csv("data/spanish_words.csv")

data = df.to_dict('records')

new_words = []
score = 0
max_score = len(data)
spanish_word = None
english_word = None
data_entry = None

def save_files():
    update = messagebox.askyesno(title="Goodbye", message="Do you want to update words based on this session?")

    if update:
        df = pandas.DataFrame(new_words)
        file = open("data/new_spanish_words_to_learn.csv", mode="w")
        file.close()
        df.to_csv("data/new_spanish_words_to_learn.csv", index=False)
    
    window.destroy()

def unfold_card(english_word):
    card.itemconfig(card_image, image=card_back)
    card.itemconfig(title_text, fill='white', text="English")
    card.itemconfig(word_text, fill='white', text=english_word)
    card.itemconfig(score_text, fill='white')

def change_word_right():
    global score
    card.itemconfig(score_text, text=f"{score}/{max_score}")

    if score == max_score:
        messagebox.showinfo(message="No more cards!")
        return

    score += 1

    global data, spanish_word, english_word, data_entry

    if score > 1:
        data.remove(data_entry)

    data_entry = random.choice(data)
    spanish_word = data_entry['Spanish']
    english_word = data_entry['English']

    card.itemconfig(card_image, image=card_front)
    card.itemconfig(title_text, fill='black', text="Spanish")
    card.itemconfig(word_text, fill='black', text=spanish_word)
    card.itemconfig(score_text, fill='black')

    window.after(TIME_UNTILL_FOLDING, unfold_card, english_word)

def change_word_wrong():
    global score, new_words, spanish_word, english_word
    card.itemconfig(score_text, text=f"{score}/{max_score}")

    new_words.append({"Spanish":spanish_word, "English":english_word})

    if score == max_score:
        messagebox.showinfo(message="No more cards!")
        return

    score += 1

    global data, data_entry
    data.remove(data_entry)        

    data_entry = random.choice(data)
    spanish_word = data_entry['Spanish']
    english_word = data_entry['English']

    card.itemconfig(card_image, image=card_front)
    card.itemconfig(title_text, fill='black', text="Spanish")
    card.itemconfig(word_text, fill='black', text=spanish_word)
    card.itemconfig(score_text, fill='black')

    window.after(TIME_UNTILL_FOLDING, unfold_card, english_word)

window = Tk()
window.protocol("WM_DELETE_WINDOW", save_files)
window.title("Spanish Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

card = Canvas(height=IMAGE_HEIGHT, width=IMAGE_WIDTH, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card.create_image(IMAGE_WIDTH //2, IMAGE_HEIGHT//2, image=card_front)
title_text = card.create_text(400, 150, text="Spanish", font=TITLE_FONT)
word_text = card.create_text(400, 263, text="", font=WORD_FONT)
score_text = card.create_text(400, 400, text="", font=SCORE_FONT)
card.grid(column=0, row=0, columnspan=2)

v_button_image = PhotoImage(file="images/right.png")
v_button = Button(image=v_button_image, relief='flat', highlightthickness=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, bd=0, command=change_word_right)
v_button.grid(column=0, row=1)

x_button_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_button_image, bg=BACKGROUND_COLOR, highlightthickness=0, relief='flat', activebackground=BACKGROUND_COLOR, bd=0, command=change_word_wrong)
x_button.grid(row=1, column=1)

change_word_right()

window.mainloop()