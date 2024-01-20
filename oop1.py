class Animal:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def show_details(self):
        print(f"Животное {self.name} имеет {self.count} ног")

obj_animal = Animal('cow', '4')
obj_animal.show_details()