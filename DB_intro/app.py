from flask import Flask, render_template
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







if __name__ == '__main__':
    app.run(debug=True)
