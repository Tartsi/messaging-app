from app import app
import sqlite3

"""
This module makes changes to the database
"""
DATABASE_NAME = 'database.db'

# SECURITY NOTIFICATION: Functions use string formatting to create Queries, instead of properly sanitizing
# or parameterizing the user input. This leaves an opening for SQL-injections. These functions directly manage the database
# thus potential SQL-injections here could cause damage to the database in terms of database integrity.


def add_user(username, password, admin_status=0):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:

        # SECURITY NOTIFICATION: Passwords are stored directly into the database without any hashing!
        # SOLUTION: Use password hashing algorithms such as bcrypt

        # Example:

        # import bcrypt
        # hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # then use this hashed_password when inserting password into the database!

        # SQL-INJECTION SOLUTION: Properly parameterize user inputs when creating SQL-queries

        # Example:

        # query = "INSERT INTO users
        #          (username, password, admin)
        #          VALUES
        #          (?, ?, ?)"

        # cursor.execute(query, (username, password, admin_status))

        sql = f"INSERT INTO users (username, password, admin) " \
            f"VALUES ('{username}', '{password}', '{admin_status}')"
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


def delete_user(id):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:

        sql = f"DELETE FROM users WHERE id = '{id}'"
        cursor.execute(sql)
        conn.commit()
        conn.close()
        return True

    except Exception as error:

        print(f"Error occurred when trying to delete user: {error}")
        conn.rollback()
        conn.close()
        return False


def delete_message(id):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:

        sql = f"DELETE FROM messages WHERE id = '{id}'"
        cursor.execute(sql)
        conn.commit()
        conn.close()
        return True

    except Exception as error:

        print(f"Error occurred when trying to delete message: {error}")
        conn.rollback()
        conn.close()
        return False


def send_message(sender_id, receiver_id, content):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # SQL-INJECTION SOLUTION: Properly parameterize user inputs when creating SQL-queries
    #
    # Example:

    # query = "INSERT INTO messages
    #          (sender_id, receiver_id, content)
    #          VALUES
    #          (?, ?, ?)"

    # cursor.execute(query, (sender_id, receiver_id, content))
    try:

        sql = f"INSERT INTO messages (sender_id, receiver_id, content) " \
            f"VALUES ('{sender_id}', '{receiver_id}', '{content}')"
        cursor.execute(sql)
        conn.commit()
        conn.close()
        return True

    except Exception as error:

        print(f"Error occurred when trying to send a message: {error}")
        conn.rollback()
        conn.close()
        return False
