from flask import Flask, render_template, request, flash, redirect, url_for, session, escape, g
from functools import wraps
import mongo
import tvmaze

app = Flask(__name__)
##un = None
app.secret_key = "super_secret_shhh"

@app.route("/", methods=["POST", "GET"])
def index():
    if "username" in session:
        return render_template("index.html", username = session["username"])
    return render_template("landing.html", searchbar=True)

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirmpw = request.form["confirmpw"]
        if mongo.validusername(username):
            if password == confirmpw:
                mongo.adduser(username, password)
                return url_for("index", message = "Register Successful")
            else:
                return render_template("signup.html", message = "Passwords do not match. Please try again.")
        else:
            return render_template("signup.html", message = "That username is already taken. Please try again.")
    return render_template("signup.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if "username" in session: #just for logout purposes for now, will change later
        del session["username"]
        return redirect("/")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if mongo.checkcombo(username, password):
            session["username"] = username
            return redirect("/")
        else:
            return render_template("login.html", message = "Incorrect username or password. Please try again.")
    return render_template("login.html")

@app.route("/search", methods=["POST", "GET"])
def search():
    #tvmaze.getShowSearch(query)
    showSearch = tvmaze.getShowSearch('girl')
    titles = []
    for item in showSearch: 
        titles.append(item[0])
    #showinfo = getShowInfo('1')
    #return render_template("search.html")
    #return redirect("/")
    return render_template("throwaway.html", titles=titles)

@app.route("/profile", methods=["POST", "GET"])
def profile():
    if "username" in session:
        return render_template("profile.html", username = session["username"])
    return redirect("/")

    
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
