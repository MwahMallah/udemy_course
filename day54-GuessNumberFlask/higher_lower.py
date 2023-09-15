from flask import Flask
import random

app = Flask(__name__)
random_num = random.randint(0, 9)

def apply_style(callback):
    def wrapper(user_number):
        text = callback(user_number)
        if text == "Too low, try again!":
            return '<h1 style="color: red;">' + text + '</h1>' \
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
        elif text == "Too high, try again!":
            return '<h1 style="color: purple;">' + text + '</h1>'\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
        elif text == "You found me!":
            return '<h1 style="color: green;">' + text + '</h1>'\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    return wrapper

@app.route("/")
def start_game():
    return '<div style="height:90vh; display: flex; align-items: center; justify-content: center; flex-direction: column;"><h1>Guess a number between 0 and 9</h1>'\
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" style="height: 200px; text-align: center;"></div>'

@app.route("/<int:user_number>")
@apply_style
def check_user_number(user_number):
    if user_number < random_num:
        return "Too low, try again!"
    elif user_number > random_num:
        return "Too high, try again!"
    else: 
        return "You found me!"


if __name__ == '__main__':
    app.run(debug=True)

