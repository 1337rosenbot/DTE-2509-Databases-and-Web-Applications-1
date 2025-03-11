# Common name for files app.y, main.py, __init__.py
from flask import Flask, render_template, url_for

app = Flask(__name__) # Create the Flask application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, Flask!'

@app.route('/programming')
def prog():
    languages = [
        "Python",
        "Swiftt",
        "C++",
        "C#",
        "Java",
        "Kotlin"
    ]
    return render_template('prog.html', prog_lang=languages)






if __name__ == '__main__':
    app.run(debug=True) # Run the Flask application