from abc import ABC, abstractmethod

# Car interface
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

# Concrete car classes
class Sedan(Car):
    def drive(self):
        print("Driving a Sedan car.")

class SUV(Car):
    def drive(self):
        print("Driving an SUV car.")

class Hatchback(Car):
    def drive(self):
        print("Driving a Hatchback car.")

# Abstract factory
class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

# Concrete factories
class SedanFactory(CarFactory):
    def create_car(self):
        return Sedan()

class SUVFactory(CarFactory):
    def create_car(self):
        return SUV()

class HatchbackFactory(CarFactory):
    def create_car(self):
        return Hatchback()

# Main program
def manufacture_car(factory):
    car = factory.create_car()
    car.drive()

# Creating and driving different cars
factories = [
    SedanFactory(),
    SUVFactory(),
    HatchbackFactory()
]

for factory in factories:
    manufacture_car(factory)