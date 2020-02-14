from src import app
from flask import render_template, request
from .static.email import send_email

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("home.html", login=False)

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        message = request.form.get("message")
        name = request.form.get("name")
        send_email(str(name), str(message))
    return render_template("about.html")

@app.route("/why")
def why():
    return render_template("why.html")

@app.route("/members")
def members():
    return render_template("members.html")

@app.route("/visit", methods=["GET", "POST"])
def visit():
    if request.method == "POST":
        message = request.form.get("message")
        name = request.form.get("name")
        send_email(str(name), str(message))
    return render_template("visit.html")

@app.route("/form", methods=["GET", "POST"])
def email():
    if request.method == "POST":
        message = request.form.get("message")
        name = request.form.get("name")
        send_email(str(name), str(message))
    return render_template("contact-form.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
