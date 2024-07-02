#Inheritance - Multilevel

class grandfather():
    grandfathername = "nana"

    def grandfathermethod(self):
        print("I am grandfather")


class father(grandfather):
    fathername = "dada"

    def fathermethod(self):
        print("I am father")

class son(father):
    sonname = "son"

    def sonmethod(self):
        print("I am son")

#create object for son which inherited father which again inherited grandfather - Multilevel

surya = son()
print(surya.sonname)
surya.sonmethod()
print(surya.fathername)
surya.fathermethod()
print(surya.grandfathername)
surya.grandfathermethod()

