from flask import Flask, render_template, redirect, request, session

from database_helper import DbHelper
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    if not session.get("username"):
        return redirect("/login")
    return render_template("index.html")


# hitting this route set's up the database config if there's no database
# with the name mentioned in the database_helper.py file
@app.route("/setup")
def setup():
    helper = DbHelper()
    helper.setup_database()
    return "<h3>Database is configured. You can use the app.</h3>"


@app.route("/register", methods=["POST", "GET"])
def register():
    # if the session is set, redirect to main page
    if session.get("username"):
        return redirect("/")
    if request.method == "POST":
        helper = DbHelper()
        username = request.form.get("username")
        if not helper.username_exists(username):
            password = request.form.get("password")
            helper.register_user(username, password)
            # now redirect to the login screen with a success message
            helper.close()
            return render_template("login.html", message="you've been registered. now log in.")
        else:
            helper.close()
            return render_template("register.html", message="That username is already taken. try something else.")
    else:
        return render_template("register.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    # if the session is set, redirect to main page
    if session.get("username"):
        return redirect("/")
    if request.method == "POST":
        helper = DbHelper()
        # check if the username exists
        username = request.form.get("username")
        password = request.form.get("password")
        # check if the username exists
        if helper.username_exists(username):
            # check if the password is correct
            if helper.password_matches(username, password):
                # set the session and redirect to main page
                session["username"] = request.form.get("username")
                # redirect to the main page
                return redirect("/")
            else:
                # render the login page with an error message saying password is incorrect
                return render_template('login.html', message="incorrect password. try again")
        else:
            # render the login page with a message saying unknown username
            return render_template("login.html", message="unknown username. try again.")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/login")


# finally, start the server
app.run(port=10000)
