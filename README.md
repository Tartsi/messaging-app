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

- Users can delete messages from their inbox.

6. Admin Page:

- Admin-status accounts can delete registered users

### Security Notifications:

- Notification in the database table setup file. The password field of users should use proper password hashing, instead of plaintext passwords for storing passwords. This practice protects users passwords incase the database is compromised.
- App secret key is too short, common and generally insecure. Also it is directly stored in a public, visible file for anyone to see.
- No CSRF protection used in index.html login-form.
- Input checks for registration form are not secure enough and only exist client-side.
- Input check for message cont when sending messages is not secure enough and only exist client-side.
- Admin password is left visible in the JavaScript-file. It is also weak and thus open to brute force attacks.
- Admin page is accessible directly from the URL.
- Functions such as adding user use string formatting to create queries, instead of properly sanitizing or parameterizing the user input. This leaves an opening for SQL-injections. Also added extra security-related information related to
fetching data from the database, namely using (*), instead of naming specific columns.
- Passwords are stored directly into the database with no hashing whatsoever.
