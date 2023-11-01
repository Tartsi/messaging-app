from flask import Flask

app = Flask(__name__)
app.secret_key = "secret_key1234"
# Security notification: The key should be more secure and way more random.
# This is more of a "theoretical" and not a "realistic" security flaw, not in this form anyway.
