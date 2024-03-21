# How to run the application:

### Download

- Clone the project *"https://github.com/Tartsi/messaging-app"*

### Setup

- Navigate to the root directory (messaging-app)

- OPTIONAL: Activate a virtual environment.

- Install required dependencies

```bash
pip install -r ./requirements.txt
```

- Run the database_setup.py-file from terminal or directly from the file database_setup.py

```bash
python/python3 database_setup.py
```

- This should create a new file 'database.db' in the directory.

- Run the application from the terminal or directly from the file routes.py

```bash
python/python3 routes.py
```

- This starts the application. You can now test out the application according to the definition.md-file. Admin-password is required to create admin-status accounts, and is located in the register.js-file!
