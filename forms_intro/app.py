from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash
import secrets
from save_file import save_to_file

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/sign_up")
def sign_up():
    return render_template('sign_up.html')

@app.route("/registration", methods=["GET", "POST"])
def registration():

    if request.method == "POST":
        req = request.form

        firstname = req["firstname"]
        lastname = req["lastname"]
        e_mail = req["e_mail"]
        password = req["password"]
        confirm_password = req["confirm_password"]

        if password == confirm_password:
            hashed_password = generate_password_hash(password)
            save_to_file(firstname, lastname, e_mail, hashed_password)

            flash("Registration complete")
            flash("Welcome!")

            return render_template("index.html")
        
        else:
            flash("Password does not match")
            return render_template("sign_up.html")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
