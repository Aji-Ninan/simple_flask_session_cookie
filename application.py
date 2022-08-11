from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
# This is specific only to the library called Flask session, and that library is going to enable hand stamps
app.config["SESSION_TYPE"] = "filesystem"
#file system is just fancy speak for the hard drive(database)
Session(app)

@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #To remember that user logged in
        name = request.form.get("name")
        session["name"] = name
        #Redirect user to /
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")