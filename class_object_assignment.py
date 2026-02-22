# =========================================================
# Assignment 1:
# Create a class named `Car` with attributes `make`, `model`,
# and `year`. Create an object and print its attributes.
# =========================================================

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("BMW", "X5", 1998)
print(car1.make, car1.model, car1.year)


# =========================================================
# Assignment 2:
# Add a method named `start_engine` to the `Car` class.
# Create an object and call the method.
# =========================================================

class Car:
    def __init__(self, make):
        self.make = make

    def start_engine(self):
        print(f"{self.make} engine started.")

my_car = Car("Audi")
my_car.start_engine()


# =========================================================
# Assignment 3:
# Create a class named `Student` with attributes `name`
# and `age`. Initialize using constructor.
# =========================================================

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Kaif", 21)
print(student1.name, student1.age)


# =========================================================
# Assignment 4:
# Create a class named `BankAccount` with private attributes
# `account_number` and `balance`. Add deposit, withdraw and
# get_balance methods.
# =========================================================

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1, 10000)
account.withdraw(1000)
print(account.get_balance())


# =========================================================
# Assignment 5:
# Create base class `Person` and derived class `Employee`
# that adds `employee_id`.
# =========================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

emp = Employee("Rahul", 25, 101)
print(emp.name, emp.age, emp.employee_id)


# =========================================================
# Assignment 6:
# Override the `__str__` method in `Employee`.
# =========================================================

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.employee_id}"

emp = Employee("Rahul", 25, 101)
print(emp)


# =========================================================
# Assignment 7:
# Create `Address` class and use it inside `Person`
# (Composition).
# =========================================================

class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

class PersonWithAddress:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

addr = Address("Qureshiyan", "Sikar", 332001)
person = PersonWithAddress("Kaif", 21, addr)
print(person.address.city)


# =========================================================
# Assignment 8:
# Create a class `Counter` with class variable `count`.
# Increment count each time object is created.
# =========================================================

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.get_count())


# =========================================================
# Assignment 9:
# Create a class `MathOperations` with static method
# to calculate square root.
# =========================================================

import math

class MathOperations:
    @staticmethod
    def square_root(num):
        return math.sqrt(num)

print(MathOperations.square_root(25))


# =========================================================
# Assignment 10:
# Create a class `Rectangle` with private attributes
# and use properties to access them.
# =========================================================

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

rect = Rectangle(10, 20)
print(rect.length, rect.width)


# =========================================================
# Assignment 11:
# Create abstract base class `Shape` with abstract method
# `area`. Implement in `Circle` and `Square`.
# =========================================================

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

print(Circle(5).area())
print(Square(4).area())


# =========================================================
# Assignment 12:
# Overload `+` operator in `Vector`.
# =========================================================

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)


# =========================================================
# Assignment 13:
# Create custom exception `InsufficientBalanceError`
# and raise it if withdrawal exceeds balance.
# =========================================================

class InsufficientBalanceError(Exception):
    pass

class BankAccountWithException:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance!")
        self.balance -= amount

account = BankAccountWithException(1000)

try:
    account.withdraw(1500)
except InsufficientBalanceError as e:
    print("Error:", e)


# =========================================================
# Assignment 14:
# Create class `FileManager` implementing context manager
# protocol to open and close file.
# =========================================================

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print("File closed successfully.")

# Example:
# with FileManager("sample.txt", "r") as f:
#     print(f.read())


# =========================================================
# Assignment 15:
# Create `Calculator` class supporting method chaining.
# =========================================================

class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        self.value += num
        return self

    def subtract(self, num):
        self.value -= num
        return self

    def multiply(self, num):
        self.value *= num
        return self

    def divide(self, num):
        if num == 0:
            raise ValueError("Cannot divide by zero")
        self.value /= num
        return self

    def result(self):
        return self.value

calc = Calculator(10)
print(calc.add(52).multiply(2).subtract(4).divide(2).result())