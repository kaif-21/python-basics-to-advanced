# inheritance in python

#  single inheritance
# parent class
class Car:
    def __init__(self,window,doors,enginetype):
        self.window = window
        self.doors = doors
        self.enginetype = enginetype

    def drive(self):
        print(f"the person will driv the {self.enginetype} car")

car1=Car(4,5,"petrol")
car1.drive()

class Tesla(Car):
    def __init__(self,window,doors,enginetype,is_selfdriving):
        super().__init__(window,doors,enginetype)
        self.is_selfdriving = is_selfdriving

    def drive(self):
        print(f"Tesla supports{self.is_selfdriving} car")


tesla=Tesla(4,5,"petrol","petrol")
tesla.drive()


# multiple inheritance
# when a class inherit from more than one base class.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Subclass must implement this method")


class Pet:
    def __init__(self, owner):
        self.owner = owner


class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} says woof"


dog = Dog("Buddy", "Kaif")
print(dog.speak())
print(f"Owner: {dog.owner}")
