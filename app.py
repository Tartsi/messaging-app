from flask import Flask

app = Flask(__name__)
app.secret_key = "myapplicationssecretkey1234"
# SECURITY NOTIFICATION: The key should be more random, it is open to brute force attacks
# It should not be stored in a visible file to the public, especially as plain text!
# This leaves the application vulnerable to CSRF attacks and session hijacks.
# The key should be stored in a separate, hidden file and not directly here.
