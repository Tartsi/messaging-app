from app import app
import sqlite3

"""
This module retrieves data from the database
"""

DATABASE_NAME = 'database.db'

# CRITICAL SECURITY NOTIFICATION: Functions use string formatting to create Queries, instead of properly sanitizing
# or parameterizing the user input. This leaves an opening for SQL-injections.


def login(username, password):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:
        # Vulnerable against SQL-injections
        # No password hashing, since it has not been implemented anywhere
        # Open to brute-force attacks as there are no limits for logins anywhere
        sql_statement = (f"SELECT * FROM users WHERE username = '{username}' "
                         f"AND password = '{password}'")
        result = cursor.execute(sql_statement).fetchall()

        if bool(result):
            conn.close()
            return True

        conn.close()
        return False
    except Exception as error:
        print("Error occurred while trying to login:", error)
        conn.close()
        return False


def get_user_by_username(username):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:

        # This is especially dangerous here, usage of * and not properly sanitizing
        # the user input might open the database for some serious SQL-injection problems.
        sql_statement = f"SELECT * FROM users WHERE username = '{username}'"
        user = cursor.execute(sql_statement).fetchall()

        if bool(user):
            conn.close()
            return user

        conn.close()
        return None
    except Exception as error:
        print("Error occurred while getting user by username:", error)
        conn.close()
        return None


def get_all_users():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:

        sql_statement = f"SELECT * FROM users"
        users = cursor.execute(sql_statement).fetchall()

        if bool(users):
            conn.close()
            return users

        conn.close()
        return None
    except Exception as error:
        print("Error occurred while retrieving users:", error)
        conn.close()
        return None


def get_messages_by_sender_id(sender_id):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:

        # String formatting used, no sanitization. Vulnerable to SQL-injection
        sql_statement = (
            "SELECT users.username, messages.content "
            "FROM messages "
            "INNER JOIN users ON messages.receiver_id = users.id "
            f"WHERE messages.sender_id = '{sender_id}'"
        )
        result = cursor.execute(sql_statement).fetchall()

        if result:
            conn.close()
            return result

        conn.close()
        return None

    except Exception as error:
        print("Error occurred while getting messages from database", error)
        conn.close()
        return None


def get_messages_by_receiver_id(receiver_id):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:

        # String formatting used, no sanitization. Vulnerable to SQL-injection
        sql_statement = (
            "SELECT users.username, messages.content, messages.id "
            "FROM messages "
            "INNER JOIN users ON messages.sender_id = users.id "
            f"WHERE messages.receiver_id = '{receiver_id}'"
        )
        result = cursor.execute(sql_statement).fetchall()

        if result:
            conn.close()
            return result

        conn.close()
        return None

    except Exception as error:
        print("Error occurred while getting messages from database", error)
        conn.close()
        return None
