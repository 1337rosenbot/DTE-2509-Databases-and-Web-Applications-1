from flask import Flask, render_template, request, redirect, url_for
from database import DataBase
from movie import Movie
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

@app.route("/")
def home():
    with DataBase() as db:
        movies = [Movie(*movie) for movie in db.getAllData()]

    return render_template('index.html', movies=movies)


@app.route("/movie/<int:movie_id>")
def movie_info(movie_id):
    with DataBase() as db:
        movie_data = db.getMovieById(movie_id)
    
        if movie_data:
            movie = Movie(*movie_data)
        else:
            return "Movie not found.", 404 # Not found error code

    return render_template("movie.html", movie=movie)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        # Add new movie to db
        req = request.form

        title = req["title"]
        year = req["year"]
        country = req["country"]
        genre = req["genre"]
        age_rating = req["age_rating"]
        duration = req["duration"]
        price = req["duration"]

        # Add to db
        data = (title, year, country, genre, age_rating, duration, price)
        
        with DataBase() as db:
            db.create_movie(data)

        return redirect(url_for('home'))

    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
