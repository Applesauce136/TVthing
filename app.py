from flask import Flask, render_template, request, flash, redirect, url_for, session, escape, g
from functools import wraps
import mongo

app = Flask(__name__)
##un = None
loggedin = False
app.secret_key = "super_secret_shhh"

@app.route("/", methods=["POST", "GET"])
def index():
    if loggedin:
        return render_template("index.html")
    return render_template("landing.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirmpw = request.form["confirmpw"]
        if mongo.validusername(username):
            if password == confirmpw:
                mongo.adduser(username, password)
                return render_template("login.html", message = "Register Successful")
            else:
                return render_template("signup.html", message = "Passwords do not match. Please try again.")
        else:
            return render_template("signup.html", message = "That username is already taken. Please try again.")
    return render_template("signup.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if mongo.checkcombo(username, password):
            session["username"] = username
            return redirect(url_for('index'))      
        else:
            return render_template("login.html", message = "Incorrect username or password. Please try again.")
    return render_template("login.html")


def authenticate(page):
    # def decorate(f):
    #     @wraps(f)
    #     def inner(*args):
    #         if 'username' not in session:
    #             return render_template(page, message = "You need to be logged in to see this!")
    #         return f(*args)
    #     return inner
    return loggedin

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
