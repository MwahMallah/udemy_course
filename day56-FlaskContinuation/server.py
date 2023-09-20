from flask import Flask, render_template
from random import randint
from datetime import date
import requests

app = Flask(__name__)

def guess_gender(name):
    params = {
        'name': name
    }
    response =requests.get("https://api.genderize.io", params=params)
    response.raise_for_status()
    content = response.json()

    return content['gender']

def guess_age(name):
    params = {
        'name': name
    }
    response =requests.get("https://api.agify.io", params=params)
    response.raise_for_status()
    content = response.json()

    return content['age']

def get_posts():
    return requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    


@app.route("/")
def home():
    random_num = randint(1, 10)
    year = date.today().year
    return render_template("index.html", random_num=random_num, year=year)


@app.route("/guess/<name>")
def guess(name):
    gender = guess_gender(name)
    age = guess_age(name)
    return render_template("guess.html", name=name.capitalize(), gender=gender, age=age)

@app.route("/blog/<num>")
def blog(num):
    print(num)
    posts = get_posts()
    return render_template("blog.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)