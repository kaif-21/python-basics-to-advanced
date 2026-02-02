''' magic methods
Magic methods are predefined method in python that you can override to change the behavior of your object
some common magic methods include:
__init__:initializes a new instance of a class.
__str__: return a string representation of an object
__repr__: return a string representation of an object
__len__: return the length of an object
__gititem__:get an item from a container
__setitem__:set an item from a container.'''


class person:
    pass

print(dir(person))
print(person)

# basic method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f'{self.name} {self.age} years old'


    def __repr__(self):
        return f"person(name={self.name},age={self.age})"
    
person=Person("KAIF", 18)
print(person)