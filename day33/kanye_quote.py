from tkinter import *
import requests

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    background.itemconfig(quote, text=data[
"quote"])


window = Tk()
window.title("Kanye said...")
window.config(padx=50, pady=50)

background_img = PhotoImage(file="background.png")
background = Canvas(width=300, height=420)
background.create_image(150, 210, image=background_img)
quote = background.create_text(150, 207, font=("Arial", 25, "bold"), fill='white', text='Kanye Quote Goes HERE', width=250)
background.grid(column=0, row=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_btn = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_btn.grid(row=1, column=0)

window.mainloop()