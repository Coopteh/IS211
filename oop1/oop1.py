class Animal:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def show_details(self):
        print(f"Животное {self.name} имеет {self.count} ноги")

obj = Animal('корова', 4)
obj.show_details()

