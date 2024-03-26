from app import app
import sqlite3

"""
This module retrieves data from the database
"""

DATABASE_NAME = 'database.db'

# SECURITY NOTIFICATION: Database fetching functions utilize * when retrieving data
# This opens the database tables for excessive data exposure risk
#
# SECURITY NOTIFICATION: Database fetching functions use string formatting to create queries

# SOLUTION: Only retrieve data from necessary columns in the database tables
# SOLUTION: Properly sanitize user inputs


def login(username, password):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:
        # Usage of * might open the database for excessive data exposure problems.
        # Unsafe user input handling

        # SQL-INJECTION SOLUTION: Properly parameterize user inputs when creating SQL-queries
        # DATA EXPOSURE SOLUTION: Only retrieve data from necessary columns
        #
        # Example for both:

        # sql_statement = """SELECT id, username, admin_status
        #                  FROM users
        #                  WHERE username = ?"""

        # search_parameters = (username)
        # result = cursor.execute(sql_statement, search_parameters)

        sql_statement = (f"SELECT * FROM users WHERE username = '{username}' "
                         f"AND password = '{password}'")
        result = cursor.execute(sql_statement).fetchall()

        # Password hashing solution:

        # This is where we would run the received password against the one stored
        # in the database:

        if bool(result):
            # stored_hash = result[0][1]
            # conn.close()
            # return bcrypt.checkpw(password.encode('utf-8'), stored_hash) // Either True or False
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

        # Usage of * might open the database for excessive data exposure problems.
        # Solution: Only retrieve data from necessary columns

        # Example:

        # sql_statement =
        # """SELECT id, username, admin_status
        # FROM users
        # WHERE username = ?"""

        # search_parameters = (username)
        # result = cursor.execute(sql_statement, search_parameters)

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
        # Usage of * might open the database for excessive data exposure problems.
        # Solution: Only retrieve data from necessary columns.

        # Example:

        # "SELECT username FROM users"

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
