from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=True, unique=True)
    author = db.Column(db.Text, nullable=True, unique=True)
    rating = db.Column(db.Float)

with app.app_context():
    db.create_all()
    # db.session.add(Books(title="Harry Potter", author="J.K. Rowling", rating="4.5"))
    db.session.commit()

