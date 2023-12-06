from flask import render_template, request, session
from models.user import User
import sqlite3
from app import app
import database_manager as dbm
import database_fetcher as dbf

# Make sure you have setup the database beforehand!
DATABASE_NAME = 'database.db'


@app.route("/testdatabase")
def test_database():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = cursor.fetchall()

    if tables:
        return "Tables exist, Database setup successful!"
    else:
        return "Error, no tables found!"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":

        username = request.form["username"]

        if dbf.get_user_by_username(username):
            return render_template("register.html", username_already_exists=True)

        password = request.form["password"]

        # Check if admin checkbox
        admin = request.form.get("admin-checkbox") == "on"

        if admin:
            # create an admin user
            admin_status = True
            user = User(username, password, admin_status)
            dbm.add_user(
                user.username, user.password, user.admin_status)
            return render_template("index.html", admin_user=True)

        # normal user
        user = User(username, password)
        dbm.add_user(user.username, user.password)

        return render_template("index.html", normal_user=True)

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = dbf.login(username, password)

        if not user:
            return render_template("index.html", user_not_found=True)

        # TODO:
        # Handle user session


if __name__ == "__main__":
    app.run(debug=True)
