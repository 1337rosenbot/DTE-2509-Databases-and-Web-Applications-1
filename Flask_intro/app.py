# Common name for files app.y, main.py, __init__.py
from flask import Flask, render_template, url_for
from book import Book

app = Flask(__name__) # Create the Flask application

@app.route('/hello')
def hello():
    return 'Hello, Flask!'


@app.route('/')  # Home page / about.html
def index():
    return render_template('index.html')


@app.route('/about_web') # Homepage
def web_dev():
    return render_template('web_dev.html')


@app.route("/about_flask") # Homepage
def intro_flask():
    return render_template('intro_flask.html')


@app.route('/recommended_books')
def books():
    rec_books = [
        Book("Flask Web Development", "Miquel Grinberg", 2018),
        Book("Python Crash Course", "Eric Matthes", 2015),
        Book("Databasesystemer", "Bjørn Kristoffersen", 2019),
        Book("Clean Code", "Martin", 2016)
    ]
    return render_template('books.html', rec_books=rec_books)


if __name__ == '__main__':
    app.run(debug=True) # Run the Flask application