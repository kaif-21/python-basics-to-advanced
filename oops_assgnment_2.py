# # Module: OOP Assignments
# ## Lesson: Polymorphism, Abstraction, and Encapsulation
# ### Assignment 1: Polymorphism with Methods
# Create a base class named `Shape` with a method `area`. Create two derived classes `Circle` and `Square` that override the `area` method. Create a list of `Shape` objects and call the `area` method on each object to demonstrate polymorphism.
import math
from tkinter.font import names


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius **2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

shapes = [Circle(5),Square(4)]

for shape in shapes:
    print("area:", shape.area())


# ### Assignment 2: Polymorphism with Function Arguments
# Create a function named `describe_shape` that takes a `Shape` object as an argument and calls its `area` method. Create objects of `Circle` and `Square` classes and pass them to the `describe_shape` function.
def describe_Shape(shape):
    print("Area:",shape.area)

c=Circle(3)
s=Square(4)

describe_Shape(c)
describe_Shape(s)
# ### Assignment 3: Abstract Base Class with Abstract Methods
# Create an abstract base class named `Vehicle` with an abstract method `start_engine`. Create derived classes `Car` and `Bike` that implement the `start_engine` method. Create objects of the derived classes and call the `start_engine` method.
# ### Assignment 4: Abstract Base Class with Concrete Methods
# In the `Vehicle` class, add a concrete method `fuel_type` that returns a generic fuel type. Override this method in `Car` and `Bike` classes to return specific fuel types. Create objects of the derived classes and call the `fuel_type` method.

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def fuel_type(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def fuel_type(self):
        return "Petrol"
class bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

    def fuel_type(self):
        return "Petrol"

car=Car()
Bike=bike()

car.start_engine()
print(car.fuel_type())

Bike.start_engine()
print(Bike.fuel_type())

# ### Assignment 5: Encapsulation with Private Attributes
# Create a class named `BankAccount` with private attributes `account_number` and `balance`. Add methods to deposit and withdraw money, and to check the balance. Ensure that the balance cannot be accessed directly.
# ### Assignment 6: Encapsulation with Property Decorators
# In the `BankAccount` class, use property decorators to get and set the `balance` attribute. Ensure that the balance cannot be set to a negative value.
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative")

acc = BankAccount("12345", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.balance)
# ### Assignment 7: Combining Encapsulation and Inheritance
# Create a base class named `Person` with private attributes `name` and `age`. Add methods to get and set these attributes. Create a derived class named `Student` that adds an attribute `student_id`. Create an object of the `Student` class and test the encapsulation.
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

student = Student("Kaif", 20, "S101")
print(student.get_name())
print(student.student_id)
# ### Assignment 8: Polymorphism with Inheritance
# Create a base class named `Animal` with a method `speak`. Create two derived classes `Dog` and `Cat` that override the `speak` method. Create a list of `Animal` objects and call the `speak` method on each object to demonstrate polymorphism.
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof")
class Cat(Animal):
    def speak(self):
        print("Wow")
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
# ### Assignment 9: Abstract Methods in Base Class
# Create an abstract base class named `Employee` with an abstract method `calculate_salary`. Create two derived classes `FullTimeEmployee` and `PartTimeEmployee` that implement the `calculate_salary` method. Create objects of the derived classes and call the `calculate_salary` method.
class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 20000

ft = FullTimeEmployee()
pt = PartTimeEmployee()

print(ft.calculate_salary())
print(pt.calculate_salary())

# ### Assignment 10: Encapsulation in Data Classes
# Create a data class named `Product` with private attributes `product_id`, `name`, and `price`. Add methods to get and set these attributes. Ensure that the price cannot be set to a negative value.
from dataclasses import dataclass

@dataclass
class Product:
    __product_id: int
    __name: str
    __price: float

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            print("Price cannot be negative")

p = Product(1, "Laptop", 50000)
print(p.price)


# ### Assignment 11: Polymorphism with Operator Overloading
# Create a class named `Vector` with attributes `x` and `y`. Overload the `+` operator to add two `Vector` objects. Create objects of the class and test the operator overloading.
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"

v1=Vector(1,2)
v2=Vector(3,4)
v3=Vector=v1+v2
print(v3)
# ### Assignment 12: Abstract Properties
# Create an abstract base class named `Appliance` with an abstract property `power`. Create two derived classes `WashingMachine` and `Refrigerator` that implement the `power` property. Create objects of the derived classes and access the `power` property.
class Appliance(ABC):

    @property
    @abstractmethod
    def power(self):
        pass

class WashingMachine(Appliance):
    @property
    def power(self):
        return "500W"

class Refrigerator(Appliance):
    @property
    def power(self):
        return "800W"

wm = WashingMachine()
rf = Refrigerator()

print(wm.power)
print(rf.power)
# ### Assignment 13: Encapsulation in Class Hierarchies
# Create a base class named `Account` with private attributes `account_number` and `balance`. Add methods to get and set these attributes. Create a derived class named `SavingsAccount` that adds an attribute `interest_rate`. Create an object of the `SavingsAccount` class and test the encapsulation.
class Account:
    def __init__(self, acc_no, balance):
        self.__acc_no = acc_no
        self.__balance = balance

    def get_balance(self):
        return self.__balance

class SavingsAccount(Account):
    def __init__(self, acc_no, balance, interest_rate):
        super().__init__(acc_no, balance)
        self.interest_rate = interest_rate

sa = SavingsAccount("A101", 10000, 5)
print(sa.get_balance())
print(sa.interest_rate)
# ### Assignment 14: Polymorphism with Multiple Inheritance
# Create a class named `Flyer` with a method `fly`. Create a class named `Swimmer` with a method `swim`. Create a class named `Superhero` that inherits from both `Flyer` and `Swimmer` and overrides both methods. Create an object of the `Superhero` class and call both methods.
class flyer:
    def fly(self):
        print("fly")

class swimmer:
    def swim(self):
        print("swim")

class superhero(flyer, swimmer):
    def fly(self):
        print("superhero flyer")
    def swim(self):
        print("superhero swimming")

hero = superhero()
hero.fly()
hero.swim()
# ### Assignment 15: Abstract Methods and Multiple Inheritance
# Create an abstract base class named `Worker` with an abstract method `work`. Create two derived classes `Engineer` and `Doctor` that implement the `work` method. Create another derived class `Scientist` that inherits from both `Engineer` and `Doctor`. Create an object of the `Scientist` class and call the `work` method.
class worker(ABC):
    @abstractmethod
    def work(self):
        pass

class engineer(worker):
    def work(self):
        return "engineer"
class doctor(worker):
    def work(self):
        return "doctor"
class scientist(engineer,doctor):
    pass

sc=scientist()
print(sc.work())