# Abstraction
# Abstraction - OOPs
# Hiding the details and showing the what is required

from abc import ABC, abstractmethod #Modules >> from <folder name> import <file>

class animal(ABC):

    def __init__(self, name):
        self.name = name
    @abstractmethod
    def sound(self):
        pass

class dog(animal):

    def sound(self):
        return "bark"

class cat(animal):

    def sound(self):
        return "meow"

class fox(animal):
    pass

dog1 = dog("rojer")
print(dog1.sound())

cat1 = cat("pussy")
print(cat1.sound())

#fox1 = fox("fox1") 
#fox1 = fox("fox1")
#TypeError: Can't instantiate abstract class fox with abstract method sound


