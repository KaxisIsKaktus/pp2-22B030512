"""
class ClassName:
    Class attributes and methods

object = ClassName()

object.attribute

object.method()
"""
class Dog:
    breed = "Unknown"

    def bark(self):
        print("Woof!")

dog = Dog()
dog.breed = "Labrador"
print(dog.breed) # Output: Labrador
dog.bark() # Output: Woof!

class Car:
    model = "mers"

    def year(self):
        for x in range(5):
            print("2010")

car = Car()
print(car.model)
car.year()