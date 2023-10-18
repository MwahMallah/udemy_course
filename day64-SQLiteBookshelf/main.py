from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html", books=Books.query.all())

@app.route("/delete")
def delete():
    book_to_delete = Books.query.filter_by(id=request.args.get('id')).first()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.get("/edit")
def edit():
    return render_template("edit.html", book=Books.query.filter_by(id=request.args.get('id')).first())

@app.post("/edit")
def edit_rating():
    new_rating = request.form['rating']
    book_to_update = Books.query.filter_by(id = request.args.get('id')).first()
    book_to_update.rating = new_rating
    db.session.commit()
    return redirect(url_for("home"))

@app.get("/add")
def add():
    return render_template("add.html")

@app.post("/add")
def add_book():
    db.session.add(Books(author=request.form['author'], title=request.form['title'], rating=request.form['rating']))
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)