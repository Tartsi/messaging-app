# Security issues and solutions:

- Issue A02:2021-Cryptographic Failures: The password field of users is in plaintext in the database. This practice leaves users vulnerable incase the database is compromised. Passwords are stored directly into the database with no hashing whatsoever from the application. In general, passwords are not properly encrypted in the application.

- Solution: Use an algorithm to generate a secure password. There are multiple possible algorithm that specialize in this, such as bcrypt for Python applications.

- Issue A02:2021-Crypthographic Failures: App secret key is too short, common and generally insecure. Also it is directly stored in a public, visible file for anyone to see.

- Solution: Use a strong, random generated value as your key for your application. Also store it in an environment-variable that is not tracked by any systems, so that it cannot be accessed by any unwanted personnel.

- Issue Cross-site Request Forgery: No CSRF protection used in forms. There is also no CSRF-token initialization for the session during login.

- Solution: Use the frameworks provided CSRF-protection across all forms. Authenticate the users session during login with a proper CSRF-token. Authenticate the users session during requests, as demonstrated in the send_messages-function.

- ~~Flaw disapproved during evaluation~~ - Fixed as of 13.05.2024

- ~~Issue A03:2021-Injection: Input checks for registration form are not secure enough and only exists client-side; Input check for message content when sending messages is not secure enough and only exists client-side.~~

- ~~Solution: Sanitize user inputs properly both client, and server-side. Make sure to use the proper security mechanism that the framework provides.~~

- Flaw disapproved during evalution; Templates do sanitization automatically by default, so this is not a flaw.

- Issue A07:2021-Identification and Authentication Failures: Admin password is left visible in the JavaScript-file. It is also weak and thus open to brute force attacks.

- Solution: Make sure to adhere to strong password policies, especially regarding admin-status passwords (12 characters long, uppercase and lowercase letters, digits, special characters). The password should also not be stored in a JavaScript-file and should be properly hashed, salted and stored within a database.

- Issue A01:2021-Broken Access Control: Admin page is accessible directly from the URL.

- Solution: Make sure to use proper authentication and authorization mechanism necessary to ensure correct access control for users.

### SQL-related:

- Issue SQL-Injection: Functions that are directly modifying the database tables such as adding users, use string formatting to create queries, instead of properly sanitizing or parameterizing the user input. This leaves an opening for SQL-injections.
- 2nd Issue Security Misconfiguration: Fetching data from the database, namely using (*), instead of naming specific columns might open the database to excessive data exposure.

Solution: Use proper sanitization methods (parameterizing) in SQL-queries that use user input. Use named columns when fetching data from the database in SQL-queries, in order to prevent any unwanted data exposure.
