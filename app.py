from flask import Flask

app = Flask(__name__)
app.secret_key = "myapplicationssecretkey1234"
# SECURITY NOTIFICATION: The key should be more random and
# it should not be stored in a visible file to the public, especially as plain text!
# This leaves the application vulnerable to CSRF attacks and session hijacks.
# The key should be stored in a separate, hidden file and not directly here.

# SOLUTION: Store the application key in a separate, hidden file such as an .env-file
# that is not tracked by any systems. If one uses GitHub for example, make sure the .env-file
# is added to the .gitignore-file.

# The application key should also be generated randomly:

# from dotenv import load_dotenv
# import os

# Generate a random key
# secret_key = os.urandom(24)

# load_dotenv() <--> Load environment variables from .env file
# app.secret_key = os.getenv('FLASK_SECRET_KEY')
