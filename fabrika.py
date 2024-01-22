from  animal import Dog, Cat, Cow

class Fabrica:
    def create(self, type):
        if type == 'Dog':
            return Dog('Собака')
        if type == 'Cat':
            return Cat('Кошка')
        if type == 'Cow':
            return Cow('Корова')
fab = Fabrica()
list_animal=[fab.create('Dog'), fab.create('Cat')]
for obj in list_animal:
    print(obj.speak())