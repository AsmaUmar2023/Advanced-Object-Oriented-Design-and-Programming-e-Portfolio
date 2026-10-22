from abc import ABC, abstractmethod
from math import pi


# Task 1: Inheritance
class Vehicle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type


class Car(Vehicle):
    def __init__(self, brand, fuel_type, num_doors):
        super().__init__(brand, fuel_type)
        self.num_doors = num_doors


# Task 2: Polymorphism and abstraction
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Task 3: Encapsulation
class BankAccount:
    def __init__(self, starting_balance=0):
        if starting_balance < 0:
            raise ValueError("Starting balance cannot be negative.")
        self.__balance = starting_balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount


# Task 4: Abstraction and method overriding
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Task 5: Constructor and destructor
class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Goodbye, {self.name}!")


if __name__ == "__main__":
    car = Car("Toyota", "hybrid", 4)
    print(f"Car: {car.brand}, {car.fuel_type}, {car.num_doors} doors")

    shapes = [Circle(3), Rectangle(4, 5)]
    for shape in shapes:
        print(f"Area: {shape.area():.2f}")

    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(25)
    print(f"Account balance: ${account.get_balance():.2f}")

    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.make_sound())

    person = Person("Alex")
    del person

