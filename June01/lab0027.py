# ploymorphism - Method Overriding
# Method overloading is not supported in python

class math():
    def calc(self):
        print("The Calc:")

class sum(math):

    def __init__(self, a , b):
        self.a = a
        self.b = b

    def calc(self):
        return self.a + self.b

class mult():

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def calc(self):
        return self.a * self.b

# Method overriding
mutiply = mult(5,6)
print(mutiply.calc())

addition = sum(3,4)
print(addition.calc())

emptyclass = math()
print(emptyclass.calc())

# Meaning: calc() methods are defined in different variants with same name > class such as sum , mult, calc
# and being utilised during the respective calls