from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/eb6cd8a5d783f501ee7d")
response.raise_for_status()

content = response.json()

@app.route("/")
def index():
    return render_template("index.html", image="home", title="Home Page", posts=content)

@app.route("/about")
def about_me():
    return render_template("about.html", image="about", title="About me")

@app.route("/contact")
def contact_me():
    return render_template("contact.html", image="contact", title="Contact me")

@app.route("/post/<int:id>")
def post(id):
    return render_template("post.html", description=content[id - 1])

if __name__ == "__main__":
    app.run(debug=True)