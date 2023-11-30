import sqlite3

"""
This module sets up the database used in the application
"""

# Define the database file name here
# The database file will be created upon execution of this setup file
# Running this setup file again will always create a new database completely (full reset)
DATABASE_NAME = 'database.db'


def create_database():

    try:

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        with open('tables.sql', 'r') as sql_file:
            sql_script = sql_file.read()

        cursor.executescript(sql_script)

        conn.commit()
        conn.close()
        print(f"Database '{DATABASE_NAME}' created successfully.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    create_database()
