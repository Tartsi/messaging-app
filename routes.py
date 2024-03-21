from flask import render_template, request, session, redirect
from models.user import User
import sqlite3
from app import app
import database_manager as dbm
import database_fetcher as dbf

# Make sure you have setup the database beforehand!
DATABASE_NAME = 'database.db'


@app.route("/testdatabase")
def test_database():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = cursor.fetchall()

    if tables:
        return "Tables exist, Database setup successful!"
    else:
        return "Error, no tables found!"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":

        username = request.form["username"]

        if dbf.get_user_by_username(username):
            return render_template("register.html", username_already_exists=True)

        password = request.form["password"]
        # You can encrypt the password here as well, now the solution is in database_manage.py-file

        # Check if admin checkbox
        admin = request.form.get("admin-checkbox") == "on"

        if admin:
            # create an admin user
            admin_status = 1
            user = User(username, password, admin_status)
            dbm.add_user(
                user.username, user.password, user.admin_status)
            return render_template("index.html", admin_user=True)

        # normal user
        user = User(username, password)
        dbm.add_user(user.username, user.password)

        return render_template("index.html", normal_user=True)

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return redirect("/")

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = dbf.login(username, password)

        if not user:
            return render_template("index.html", user_not_found=True)

        user_info = dbf.get_user_by_username(username)

        session["username"] = username
        session["user_id"] = user_info[0][0]
        session["admin_status"] = user_info[0][3]
        session["user_received"] = []
        session["user_sent"] = []
        # NO CSRF-token initialization for the session

        if session["admin_status"] == 1:
            return redirect("/admin")

        sent_messages = dbf.get_messages_by_sender_id(session["user_id"])
        received_messages = dbf.get_messages_by_receiver_id(session["user_id"])

        if received_messages:
            for message in received_messages:
                session["user_received"].append(
                    {'sender': message[0], 'content': message[1], 'id': message[2]})

        if sent_messages:
            for message in sent_messages:
                session["user_sent"].append(
                    {'receiver': message[0], 'content': message[1]})

        session.modified = True

        return redirect("/dashboard")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    # Clears only username from the session, not the entire session
    # Might not necessarily be a security flaw, but worth mentioning
    del session["username"]
    return redirect("/")


@app.route("/admin/delete/<int:id>", methods=["GET"])
def delete_user(id):

    if dbm.delete_user(id):

        return redirect("/admin")


@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "GET":

        # CRITICAL SECURITY NOTIFICATION: Broken Access Control
        # NO ADMINISTRATION CHECK: Admin-page accessible directly via the URL!

        all_users = []
        result = dbf.get_all_users()

        if result:

            for user in result:

                # Only show normal users on admin page
                if user[3] == 0:
                    all_users.append(
                        {'id': user[0], 'username': user[1], 'admin_status': user[3]})

        return render_template("admin.html", users=all_users)


@app.route("/dashboard", methods=["GET"])
def dashboard():

    if request.method == "GET":
        if "username" not in session or not dbf.get_user_by_username(session["username"]):
            return render_template("index.html", user_not_logged_in=True)

    return render_template("dashboard.html", alert=True, sent_messages=session["user_sent"], user_messages=session["user_received"], user=session["username"])


@app.route("/send_message", methods=["POST"])
def send_message():

    if request.method == "POST":

        receiver_username = request.form["recipient"]

        receiver_data = dbf.get_user_by_username(receiver_username)

        if receiver_data is not None:
            content = request.form["message"]

            if dbm.send_message(session["user_id"], receiver_data[0][0], content):
                session["user_sent"].append(
                    {'receiver': receiver_data[0][1], 'content': content})
                session.modified = True
                return render_template("dashboard.html", sent_messages=session["user_sent"], user_messages=session["user_received"], user=session["username"], message_sent=True)

        else:
            return render_template("dashboard.html", sent_messages=session["user_sent"], user_messages=session["user_received"], user=session["username"], user_not_found=True)


@app.route("/delete_message", methods=["POST"])
def delete_message():

    # CAUTION! Deleting a received message deletes message from both user and sender
    # This is due to bad design in the tables.sql (only 1 messages-table for sent and received messages)
    # Not necessarily a security issue per say, but definitely worth mentioning as a flaw

    if request.method == "POST":

        message_id = int(request.form["message_id"])

        if dbm.delete_message(message_id):

            for i, msg in enumerate(session["user_received"]):

                if msg['id'] == message_id:
                    del session["user_received"][i]
                    session.modified = True
                    break

        return render_template("dashboard.html", sent_messages=session["user_sent"], user_messages=session["user_received"], user=session["username"])


if __name__ == "__main__":
    app.run(debug=False)
