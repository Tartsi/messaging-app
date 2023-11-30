from app import app
import sqlite3

"""
This module makes changes to the database
"""
DATABASE_NAME = 'database.db'

# CRITICAL SECURITY NOTIFICATION: Functions use string formatting to create Queries, instead of properly sanitizing
# or parameterizing the user input. This leaves an opening for SQL-injections.


def add_user(username, password, admin_status=0):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:

        # SECURITY NOTIFICATION: Passwords are stored directly into the database without any hashing!

        sql = f"INSERT INTO users (username, password, admin) VALUES ('{username}', '{password}', '{admin_status}')"
        cursor.execute(sql)
        print(f"Succesfully created user: {username}")
        conn.commit()
        conn.close()
        return True

    except Exception as error:

        print(f"Error occurred when trying to add user: {error}")
        conn.rollback()
        conn.close()
        return False


def delete_user(username):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:

        sql = f"DELETE FROM users WHERE username = '{username}'"
        cursor.execute(sql)
        conn.commit()
        conn.close()
        return True

    except Exception as error:

        print(f"Error occurred when trying to delete user: {error}")
        conn.rollback()
        conn.close()
        return False


# For testing purposes only.
with app.app_context():
    pass
