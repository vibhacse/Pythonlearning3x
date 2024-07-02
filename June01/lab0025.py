# Inheritance - Multiple - supported in python , but not in java

class Father:
    def father_money(self):
        return "5"

    def home(self): #same method name used in father_money and mother_money
        return "This is from the Father"


class Mother:
    def mother_money(self):
        return "2"

    def home(self):
        return "This is from the Mother"

    def mother(self):
        return "This is Mother Method"
class Son(Mother,Father): #multiple inheritance > Son consist of both Father and Mother
    pass

# Problem - Diamond Problem - Java
# Python - Multiple Inheritance
# F,M -> S

son = Son()
son.father_money()
son.mother_money()
print(son.home()) # Method Resolution
print(son.mother())