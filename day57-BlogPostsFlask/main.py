from flask import Flask, render_template
from post import Post

posts = Post().get_posts()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("myindex.html", blog_posts = posts)

@app.route('/post/<int:id>')
def post(id):
    return render_template("post.html", blog_post = posts[id - 1])


if __name__ == "__main__":
    app.run(debug=True)
