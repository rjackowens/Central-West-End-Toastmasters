from src import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("home.html", login=False)

@app.route("/about")
def about():
    return render_template("about.html", login=False)

@app.route("/why")
def why():
    return render_template("why.html", login=False)

@app.route("/members")
def members():
    return render_template("members.html", login=False)

@app.route("/visit")
def visit():
    return render_template("visit.html", login=False)
