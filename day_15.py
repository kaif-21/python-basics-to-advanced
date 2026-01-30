# polymorphism

# base class
class Animal:
    def speak(self):
        return "Sound of the animal"

# derived class

class dog (Animal):
    def speak(self):
        return "woof woof"

# derived class
class cat(Animal):
    def speak(self):
        return "meow!"
# function that demonestrates polymorphism
def animal_speak(animal):
    return animal.speak()
Dog=dog()
Cat=cat()
print(Dog.speak())
print(Cat.speak())
animal_speak(Dog)


# polymorphism with function and method

# base class
class Shape:
    def area(self):
        return "The area of the figure"

# derived class 1
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height

# derived class 2
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius

# function that demonstrates polymorphism
def print_area(shape):
    print(f"The area of the figure is {shape.area()}")

rectangle=Rectangle(10,20)
circle=Circle(10)

print_area(rectangle)
print_area(circle)


# polymorphism with abstract base class
from abc import ABC, abstractmethod

# abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"


class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"


# polymorphic function
def start_vehicle(vehicle):
    print(vehicle.start_engine())


car = Car()
bike = Motorcycle()

start_vehicle(car)
start_vehicle(bike)
