import sqlite3

db = sqlite3.connect("books-collection.db")

cursor = db.cursor()

cursor.execute("""
        INSERT INTO "books"
        ("title", "author", "rating")           
        VALUES
        ("Harry Potter", "J.K. Rowling", "4.5");
    """)
db.commit()