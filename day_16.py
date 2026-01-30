# Encapsulation with getter and setter

class person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # getter method for name
    def get_name(self):
        return self.__name

    # setter method for name
    def set_name(self, name):
        self.__name = name

    # getter method for age
    def get_age(self):
        return self.__age

    # setter method for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age. Please enter correct age.")


Person = person("kaif", 25)

# access using getter
print(Person.get_name())
print(Person.get_age())

# modify using setter
Person.set_age(30)
print(Person.get_age())

