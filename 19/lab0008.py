#internal function - Encapsulation

def namePrint(person_name):
    age = int(input("Enter your age:"))
    def adultCheck(age):
        if age > 18:
            print("You are adult")
        else:
            print("Not adult")
    adultCheck(age)

person_name = str(input("Enter you Name:"))
namePrint(person_name)

