from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

MOVIE_URL_POSTER = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap5(app)
db = SQLAlchemy(app)

def get_movie_details(id):
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMzQ2YzBiOGQzYTFhY2ZkNjJlMDVmODNlZGQ5YmQwZiIsInN1YiI6IjY1MzJlZjBkYjI2ODFmMDBlMTNhZjZkNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pdXS_5kE-aKrf3gwftjwff_S3ws90JbTud8fQyl_q3k"
    }

    response = requests.get(f"https://api.themoviedb.org/3/movie/{id}", headers=headers)
    return response.json()

def get_movie(title):
    url = 'https://api.themoviedb.org/3/search/movie'
    params = {
        "query": title
    }

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMzQ2YzBiOGQzYTFhY2ZkNjJlMDVmODNlZGQ5YmQwZiIsInN1YiI6IjY1MzJlZjBkYjI2ODFmMDBlMTNhZjZkNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pdXS_5kE-aKrf3gwftjwff_S3ws90JbTud8fQyl_q3k"
    }

    return requests.get(url, params=params, headers=headers)

class EditForm(FlaskForm):
    rating = StringField("Your rating out of 10 e.g. 7.5", name="rating")
    review = StringField("Your review", name="review")
    submit = SubmitField("Done")

class AddForm(FlaskForm):
    title = StringField("Movie title", name='title')
    submit = SubmitField("Add movie")

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String)
    img_url = db.Column(db.String)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    movies = Movies.query.order_by(asc(Movies.rating))
    for rank, movie in enumerate(movies[::-1], 1):
        movie.ranking = rank
    return render_template("index.html", movies=movies)

@app.route("/add", methods=['POST', 'GET'])
def add_movie():
    form = AddForm()
    if form.validate_on_submit():
        title = form.title.data
        response = get_movie(title)
        movies = response.json()["results"]
        return render_template("select.html", options=movies)
    return render_template("add.html", form=form)

@app.route("/edit", methods=['POST', 'GET'])
def edit():
    form = EditForm()
    if form.validate_on_submit():
        user_movie = Movies.query.filter_by(id = request.args.get("id")).first()
        user_movie.rating = request.form.get("rating")
        user_movie.review = request.form.get("review")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)

@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    Movies.query.filter(Movies.id == movie_id).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/details")
def details():
    details = get_movie_details(id=request.args.get("id"))
    new_movie = Movies(
        title=details["title"], 
        description=details["overview"], year=details["release_date"].split("-")[0], 
        img_url=f"{MOVIE_URL_POSTER}/{details['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
