from flask import render_template, request
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


if __name__ == "__main__":
    app.run(debug=True)
