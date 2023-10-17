from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from orm import Books

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db.init_app(app)

with app.app_context():
    db.session.add(Books(title="Harry Potter without stone", author="J.J.Rowling", rating=3.1))
    result = db.session.execute(db.select(Books).where(Books.rating >= 4.5)).scalar()
    result.title = "Harry Potter and stone"
    db.session.commit()
    
