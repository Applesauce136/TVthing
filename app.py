from flask import Flask, render_template, request, flash, redirect, url_for, session, escape, g
from functools import wraps
import mongo

app = Flask(__name__)
##un = None
##loggedin = False
app.secret_key = "super_secret_shhh"

@authenticate()
@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

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
