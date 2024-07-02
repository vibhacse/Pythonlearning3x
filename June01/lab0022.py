#Inheritance - Single

class grandparent(): #base class
    grandfathername = "Kumar"

    def grandparentmethod(self):
        return "grandparent method"

class father(grandparent): #child class
    fathername = "suresh"

    def fathermethod(self):
        return "father method"


#create object for base class
GP = grandparent()
print(GP.grandfathername)
print(GP.grandparentmethod())

#create object for child class - Can access methods and variable (data members) of base class
# as its inherited

F = father()
print(F.fathername)
print(F.fathermethod())
print(F.grandfathername)
print(F.grandparentmethod())