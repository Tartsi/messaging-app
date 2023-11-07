from flask import Flask

app = Flask(__name__)
app.secret_key = "secret_key1234"
# SECURITY NOTIFICATION: The key should be more way more random.
# In this form this is more of a "theoretical" and not a "realistic" security flaw.
