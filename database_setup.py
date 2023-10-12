import sqlite3

# Define the database file name here
# The database file will be created upon execution of this setup file
DATABASE_NAME = 'database.db'

# Placeholder

# TODO: Advance the actual project and think of the potential dependencies it might have!


def create_database():

    try:

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                          id INTEGER PRIMARY KEY,
                          username TEXT,
                          password TEXT)''')

        conn.commit()
        conn.close()
        print(f"Database '{DATABASE_NAME}' created successfully.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    create_database()
