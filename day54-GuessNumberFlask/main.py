from flask import Flask

app = Flask(__name__)

def make_underline(callback):
    def underline_inner():
        typed_string = callback()
        return "<u>" + typed_string + "</u>"
    return underline_inner

def make_italic(callback):
    def italic_inner():
        typed_string = callback()
        return "<em>" + typed_string + "</em>"
    return italic_inner


def make_bold(callback):
    def bold_inner():
        typed_string = callback()
        return "<b>" + typed_string + "</b>"
    return bold_inner

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center;">Hello, World</h1>' \
    '<p>This is a paragraph</p>' \
    '<img src="https://upload.wikimedia.org/wikipedia/commons/b/bc/Juvenile_Ragdoll.jpg" style="width: 300px;">'


@app.route("/bye")
@make_italic
@make_bold
@make_underline
def bye():
    return "Bye"

@app.route("/username/<username>/<int:number>")
def greet(username, number):
    return f"Hello {username} {number}"

if __name__ == "__main__":
    app.run(debug=True)