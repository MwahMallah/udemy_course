from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///old-books-collection.db"
db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False, unique=True)
    author = db.Column(db.Text, nullable=False, unique=True)
    rating = db.Column(db.Float)

with app.app_context():
    db.create_all()

with app.app_context():
    db.session.add(Books(title="Life of Aboba", author='Dima', rating="4.5"))
    db.session.add(Books(title="Life of Boba", author='Ilya', rating="4.1"))
    db.session.commit()
