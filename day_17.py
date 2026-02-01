# Abstraction

'''Abstraction is the concept of hiding the complex implementation detail and showing only the necessary
 feature of an object.This helps in reducing programming complexity and efforts. '''

from abc import ABC, abstractmethod
# abstract base class
class Vehicle(ABC):
    def drive(self):
        print("The vehicle is used for driving")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("car engine started")

def operate_vehicle(vehicle):
    vehicle.drive()
    vehicle.start_engine()

car=Car()
print(car.drive())
