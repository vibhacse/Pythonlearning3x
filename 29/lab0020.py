#Encapsulation - Bind the data variable with the methods
#data member - class variables / instance variables
#methods - definition of function within the class
#__init__ - name of contructor of class

#public, private, protected methods inside the class

class car:
    def public(self):
        print("I am public method")

    def _private(self):
        print("I am private method")

    def __protected(self):
        print("I am protected method")

alto = car()
alto.public()

#public, __private, _protected variable inside methos of the class

class student():

    def __init__(self,studname, studgrade, studyear):
        self.name = studname #public variable
        self.__year = studyear #private variable
        self._grade = studgrade  # protected variable

student1 = student("vivek","A","2023")
student1.name

#private methods can be accessed only via public method within the class

class colors():

    def __private_method(self):
        print("This is private...")

    def public_method(self):
        self.__private_method()

check = colors()
check.public_method()

#public and private variable inside the class

class login():

    def login_cred(self, username, password):
        self.username = username
        self.__password = password

page1 = login()
page1.username
#page1._password -> not accessible outside the class
page1.login_cred("vivek","123")




