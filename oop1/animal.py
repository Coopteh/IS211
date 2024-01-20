class Animal:
    def __init__(self, name, count):
        self.__name = name
        self.__count = count

    def show_details(self):
        print(f"Животное {self.__name} имеет {self.__count} ноги")

    def get_name(self):
        return self.__name

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Cow(Animal):
    pass

obj_dog = Dog('собака', 2)
obj_cat = Cat('кот', 3)
obj_cow = Cow('корова', 5)

list1 = [obj_dog, obj_cat, obj_cow]
for obj in list1:
    obj.show_details()