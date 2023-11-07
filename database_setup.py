import sqlite3

"""
This module sets up the database used in the application
"""

# Define the database file name here
# The database file will be created upon execution of this setup file
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


def reset_database():
    try:

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Drops all tables from the database
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = cursor.fetchall()

        if len(tables) != 0:
            for table in tables:
                table_name = table[0]
                cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
                print("Dropped table", table_name)
        else:
            print("No tables to drop!")

        conn.commit()
        conn.close()
        print(f"Database '{DATABASE_NAME}' has been reset.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # reset_database()
    create_database()
