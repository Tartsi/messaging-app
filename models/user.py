class User:

    def __init__(self, username, password, admin_status=False):
        self.username = username
        self.password = password
        self.admin_status = admin_status

    def __str__(self):

        if (self.admin_status == True):
            return "User {self.username} is an admin."

        return "User {self.username} is not an admin."
