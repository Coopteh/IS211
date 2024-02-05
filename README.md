# Паттерн "Команда" (Command)
поведенческий паттерн  
позволяет инкапсулировать запрос в объекте на выполнение определенного действия,   
параметризуя объекты-команды для разных запросов, ставить запросы в очередь, логировать их и отменять.

Рассмотрим пример
```
from abc import ABC, abstractmethod
from typing import List

class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class ChiefAssistant:
    def prepare_pizza_dough(self):
        print("Ассистент подготавливает тесто для пиццы")

class Stove:
    def prepare_stove(self):
        print("Печь разогревается")

    def cooking_pizza(self):
        print("Пицца готовится в печи")

class ChiefCooker:
    def add_topping_to_pizza(self):
        print("Шеф добавляет начинку на пиццу")

class PrepareStoveCommand(ICommand):
    """Класс команды для разогрева печи"""
    def __init__(self, executor: Stove):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_stove()


class PrepareDoughCommand(ICommand):
    """Класс команды для подготовки теста пиццы"""
    def __init__(self, executor: ChiefAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_pizza_dough()

class CookingPizzaCommand(ICommand):
    """Класс команды для приготовления пиццы в печи"""
    def __init__(self, executor: Stove):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.cooking_pizza()

class AddToppingCommand(ICommand):
    """Класс команды для добавления начинки на пиццу"""

    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.add_topping_to_pizza()

class Pizzeria:
    """Класс агрегации всех команд для приготовления пиццы"""
    def __init__(self):
        self.history: List[ICommand] = []

    def addCommand(self, command: ICommand) -> None:
        self.history.append(command)

    def cook(self) -> None:
        if not self.history:
            print("Не задана очередность выполнения команд приготовления пиццы")
        else:
            for command in self.history:
                command.execute()
        self.history.clear()


if __name__ == "__main__":
    chief = ChiefCooker()
    assistant = ChiefAssistant()
    stove = Stove()
    pizzeria = Pizzeria()
    # формируем последовательность команд для приготовления пиццы
    pizzeria.addCommand(PrepareDoughCommand(assistant))
    pizzeria.addCommand(PrepareStoveCommand(stove))
    pizzeria.addCommand(AddToppingCommand(chief))
    pizzeria.addCommand(CookingPizzaCommand(stove))
    # запускаем процесс приготовления пиццы
    pizzeria.cook()
```

В этом примере:
- ICommand - определяет общий интерфейс для всех команд.
- ChiefAssistant - получатель команды, который фактически выполняет действие.
- PrepareDoughCommand - конкретная реализация команды для подготовки теста.
- Pizzeria - класс агрегации всех команд для приготовления пиццы,
который назначает команду и запускает её выполнение.
 
Паттерн "Команда" создает обобщенную систему обработки команд.

### Задание
- создайте класс Courier, который доставляет пиццу клиенту
- команду CourierDeliveryCommand реализующую доставку пиццы курьером
- добавьте новую команду в процесс работы класса Pizzeria

