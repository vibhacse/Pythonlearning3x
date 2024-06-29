#class and methods

class login():
    email = None
    password = None

    def __init__(self, username, password):
        self.email = username
        self.password = password

    def login_confirm(self):
        if self.email == "vivek@gmail.com":
            print("Valid username")
        else:
            print("Invalid username, Login Failed!")
        if self.password == "Pass123":
            print("Valid password")
        else:
            print("Invalid password, Login Failed!")

user1 = login("vivek@gmail.com","Pass123")
user1.login_confirm()

user2 = login("bhar@123","pas345")
user2.login_confirm()

user3 = login("vivek@gmail.com","pio")
user3.login_confirm()

user4 = login("hjh","Pass123")
user4.login_confirm()
