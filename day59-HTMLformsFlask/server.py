from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["post"])
def login():
    return render_template("login.html", username=request.form['username'], password=request.form['password'])


if __name__ == "__main__":
    app.run(debug=True)