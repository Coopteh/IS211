class Animal:
    def get_name(self):
        return self.__name
    def __init__(self, name):
        self.__name = name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return ("гав")

class Cat(Animal):
    def speak(self):
        return ("мяу")

class Cow(Animal):
    def speak(self):
        return ("му")


