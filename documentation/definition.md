# Requirements Specification:

- Intented functionality without security issues:

1. User Registration and Login:

- Users are able to register and login/logout with their account.
- Admin users are able to register with admin password.

2. Send Messages:

- Users are able to send messages to other registered users.

3. View Inbox:

- Users can view messages sent to them.

4. View Sent Messages:

- Users can view messages they have sent.

5. Delete Messages:

- Users can delete messages from their inbox.

6. Admin Page:

- Admin-status accounts can delete registered users.

### Known Issues in the application:

- Sent messages will also be deleted from sending users sent messages if the receiving user deletes the message from receiving users inbox.
- Admin-status accounts cannot send/receive messages, unless they manually modify the URL to access dashboard, which is not intended.
