# Cyber Security Base Project #1

### Messaging Application

- Simple minimalistic-scale messaging application, INTENTED to include security flaws, using Flask, Python and SQLite3.
- README.md will be updated along with the projects creation.

### Requirements Specification:

- Intented functionality:

1. User Registration and Login:

- Users are able to register and login/logout with their account.

2. Send Messages:

- Users are able to send messages to other registered users.

3. View Inbox:

- Users can view messages sent to them.

4. View Sent Messages:

- Users can view messages they have sent.

5. Delete Messages:

- Users can delete messages from their inbox/sent messages list.

### Security Notifications:

- Notification in the database table setup file. The password field of users should use proper password hashing, instead of plaintext passwords for storing passwords. This practice protects users passwords incase the database is compromised.
- App secret key is way too short, common and generally insecure.
- No CSRF protection used in index.html login-form.
- Input checks for registration form are not secure enough.