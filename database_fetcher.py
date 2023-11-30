from app import app
import sqlite3

"""
This module retrieves data from the database
"""

DATABASE_NAME = 'database.db'

# CRITICAL SECURITY NOTIFICATION: Functions use string formatting to create Queries, instead of properly sanitizing
# or parameterizing the user input. This leaves an opening for SQL-injections.


def get_user_by_username(username):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:

        # This is especially dangerous here, usage of * and not properly sanitizing
        # the user input might open the database for some serious SQL-injection problems.
        sql_statement = f"SELECT * FROM users WHERE username = '{username}'"
        user = cursor.execute(sql_statement).fetchone()

        if bool(user):
            return user
        else:
            return None

    except Exception as error:
        print("Error occurred while getting user by username:", error)
        conn.close()
        return None


with app.app_context():
    pass
