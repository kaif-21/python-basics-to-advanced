# =====================================================
# Module: Inheritance Assignments
# Lesson: Single and Multiple Inheritance
# =====================================================

# -----------------------------------------------------
# Assignment 1: Single Inheritance Basic
# Create a base class named Animal with attributes name and species.
# Create a derived class named Dog that inherits from Animal and adds
# an attribute breed. Create an object of the Dog class and print its attributes.
# -----------------------------------------------------
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def __str__(self):
        return f"{self.name}, {self.species}, {self.breed}"

dog = Dog("Buddy", "Mammal", "Labrador")
print(dog)


# -----------------------------------------------------
# Assignment 2: Method Overriding in Single Inheritance
# Override the __str__ method in Dog class and print the object.
# -----------------------------------------------------
print(str(dog))


# -----------------------------------------------------
# Assignment 3: Single Inheritance with Additional Methods
# Add a method bark in Dog class and call it.
# -----------------------------------------------------
class DogWithBark(Dog):
    def bark(self):
        print("Woof Woof")

dog2 = DogWithBark("Rocky", "Mammal", "Bulldog")
dog2.bark()


# -----------------------------------------------------
# Assignment 4: Multiple Inheritance Basic
# Create Walker and Runner classes with walk and run methods.
# Create Athlete class inheriting from both and call both methods.
# -----------------------------------------------------
class Walker:
    def walk(self):
        print("Walking")

class Runner:
    def run(self):
        print("Running")

class Athlete(Walker, Runner):
    pass

athlete = Athlete()
athlete.walk()
athlete.run()


# -----------------------------------------------------
# Assignment 5: Method Resolution Order (MRO)
# Override walk in Athlete and use super() to call Walker's walk.
# -----------------------------------------------------
class AthleteMRO(Walker, Runner):
    def walk(self):
        print("Athlete walking")
        super().walk()

athlete_mro = AthleteMRO()
athlete_mro.walk()


# -----------------------------------------------------
# Assignment 6: Multiple Inheritance with Additional Attributes
# Add training_hours attribute and train method in Athlete class.
# -----------------------------------------------------
class AthleteTrain(Walker, Runner):
    def __init__(self, training_hours):
        self.training_hours = training_hours

    def train(self):
        print(f"Training for {self.training_hours} hours")

athlete_train = AthleteTrain(5)
athlete_train.train()


# -----------------------------------------------------
# Assignment 7: Diamond Problem in Multiple Inheritance
# Observe method resolution order.
# -----------------------------------------------------
class A:
    def show(self):
        print("Hello")

class B(A):
    def show(self):
        print("From B")

class C(A):
    def show(self):
        print("From C")

class D(B, C):
    pass

d = D()
d.show()
print(D.mro())


# -----------------------------------------------------
# Assignment 8: Using super() in Single Inheritance
# Initialize attributes using super().
# -----------------------------------------------------
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

circle = Circle("Red", 5)
print(circle.color, circle.radius)


# -----------------------------------------------------
# Assignment 9: Using super() in Multiple Inheritance
# Create Person, Employee, and Manager classes.
# -----------------------------------------------------
class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

class Manager(Person, Employee):
    def __init__(self, name, employee_id):
        Person.__init__(self, name)
        Employee.__init__(self, employee_id)

manager = Manager("Kaif", 101)
print(manager.name, manager.employee_id)


# -----------------------------------------------------
# Assignment 10: Method Overriding and super()
# Override start method in Car and call Vehicle's start.
# -----------------------------------------------------
class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        print("Car starting")
        super().start()

car = Car()
car.start()


# -----------------------------------------------------
# Assignment 11: Multiple Inheritance with Different Methods
# Create Flyer, Swimmer, and Superhero classes.
# -----------------------------------------------------
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Superhero(Flyer, Swimmer):
    pass

hero = Superhero()
hero.fly()
hero.swim()


# -----------------------------------------------------
# Assignment 12: Complex Multiple Inheritance
# Initialize attributes a, b, and c.
# -----------------------------------------------------
class Base1:
    def __init__(self, a):
        self.a = a

class Base2:
    def __init__(self, b):
        self.b = b

class Derived(Base1, Base2):
    def __init__(self, a, b, c):
        Base1.__init__(self, a)
        Base2.__init__(self, b)
        self.c = c

obj = Derived(1, 2, 3)
print(obj.a, obj.b, obj.c)


# -----------------------------------------------------
# Assignment 13: Checking Instance Types with Inheritance
# Use isinstance() to check object types.
# -----------------------------------------------------
class AnimalBase:
    pass

class Cat(AnimalBase):
    pass

animal = AnimalBase()
cat = Cat()

print(isinstance(animal, AnimalBase))
print(isinstance(cat, AnimalBase))
print(isinstance(cat, Cat))


# -----------------------------------------------------
# Assignment 14: Polymorphism with Inheritance
# Demonstrate polymorphism using Bird, Parrot, and Penguin.
# -----------------------------------------------------
class Bird:
    def speak(self):
        print("Bird sound")

class Parrot(Bird):
    def speak(self):
        print("Parrot speaks")

class Penguin(Bird):
    def speak(self):
        print("Penguin sound")

birds = [Parrot(), Penguin(), Bird()]
for b in birds:
    b.speak()


# -----------------------------------------------------
# Assignment 15: Combining Single and Multiple Inheritance
# Create Device, Phone, Camera, and Smartphone classes.
# -----------------------------------------------------
class Device:
    def __init__(self, brand):
        self.brand = brand

class Phone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

class Smartphone(Phone, Camera):
    def __init__(self, brand, model, resolution):
        Phone.__init__(self, brand, model)
        Camera.__init__(self, resolution)

smart = Smartphone("Samsung", "Galaxy", 108)
print(smart.brand, smart.model, smart.resolution)



