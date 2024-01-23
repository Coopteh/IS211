# Описание
Изучаем паттерн проектирования "Строитель" (Builder)

файл model.py
```
# Класс автомобиль
class Car:
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price

    def __str__(self):
        return f"Авто: цвет - {self.color}, модель - {self.model}, цена = {self.price} руб"
```
файл builder.py
```
from model import *

# Класс Строителя (Builder)
class CarBuilder:
    def __init__(self):
        self.car = Car("", "", "")

    def set_model(self, model):
        self.car.model = model

    def set_color(self, color):
        self.car.color = color

    def set_price(self, price):
        self.car.price = price
        if (self.car.color == "красный"):
            self.car.price = price * 1.1

    def get_car(self):
        return self.car
```
файл manager.py
```
# Класс управления
class CarManager:
    def __init__(self, builder):
        self.builder = builder

    def construct_sports_car(self):
        self.builder.set_model("Sports Car")
        self.builder.set_color("белый")
        self.builder.set_price(10000000)

    def construct_black_vesta_car(self):
        self.builder.set_model("LADA Vesta")
        self.builder.set_color("черный")
        self.builder.set_price(1000000)

    def construct_red_vesta_car(self):
        self.builder.set_model("LADA Vesta")
        self.builder.set_color("красный")
        self.builder.set_price(1000000)
```
класс main.py
```
from model import *
from builder import *
from manager import *

builder = CarBuilder()
manager = CarManager(builder)

manager.construct_sports_car()
sport_car = builder.get_car()
print(sport_car)
```

# Задача
В pyCharm cоздать новый проект Builder (в папке PycharmProjects)  
для модели двери (Door) с полями материал и цена  
создать строитель и менеджер  
проверить для золотой двери и деревянной (в случае золотой цена увеличивается в 2 раза)  
