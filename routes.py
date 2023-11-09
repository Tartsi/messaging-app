from flask import render_template, request
from models import user
import sqlite3
from app import app

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

        # if username already exists
        # TODO: CHECK
        # return render_template("register.html", username_already_exists=True)

        password = request.form["password"]

        # Check if admin checkbox
        admin = request.form.get["admin-checkbox"] == "on"

        if admin:
            # create an admin user
            admin_status = 1
            user = user.User(username, password, admin_status)
            return render_template("index.html", admin_user=True)

        # normal user
        user = user.User(username, password)

    return render_template("index.html", normal_user=True)


if __name__ == "__main__":
    app.run(debug=True)
