#Method overriding with super keyword

class father():

    def home(self):
        print("1 BHK")

class son(father):

    def home(self):
        super().home() # super represents base / parent class methods
        print("No Home")

kumar = son()
kumar.home()

fathers = father()
fathers.home()