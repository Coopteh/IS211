# Паттерн "Декоратор" (Composite) 
динамически добавляет объекту новые обязанности
структурный паттерн  

**Назначение:**  
Иногда нужно добавить новые обязанности объекту, а не классу в целом.   
То есть сделать это динамически (композицией, через передачу объекта), а не статически.
Альтернатива наследованию (созданию подклассов)

Рассмотрим пример
```
# Интерфейс "Компонент"
class Coffee:
    def cost(self):
        pass

    def description(self):
        pass


# Конкретная реализация "Компонент"
class AmericanoCoffee(Coffee):
    def cost(self):
        return 100

    def description(self):
        return "Кофе Американо"


# Абстрактный декоратор
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._decorated_coffee = coffee

    def cost(self):
        return self._decorated_coffee.cost()

    def description(self):
        return self._decorated_coffee.description()


# Декоратор добавки "Молоко"
class Milk(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def cost(self):
        return self._decorated_coffee.cost() + 15

    def description(self):
        return self._decorated_coffee.description() + ", с молоком"
```
Использование:
```
def main():
    my_coffee = AmericanoCoffee()
    print(f"Цена: {my_coffee.cost()}, Описание: {my_coffee.description()}")

    milk_coffee = Milk(my_coffee)
    print(f"Цена: {milk_coffee.cost()}, Описание: {milk_coffee.description()}")


if __name__ == "__main__":
    main()
```
В этом примере:
- Coffee представляет интерфейс для напитков, предоставляющий методы cost и description.  
- SimpleCoffee представляет конкретную реализацию напитка.  
- CoffeeDecorator - абстрактный класс декоратора, содержащий ссылку на оборачиваемый объект.  
- Milk - конкретный декоратор, предоставляющий функциональность добавки молока.  
 
Такой подход позволяет клиентскому коду работать с отдельными объектами и их контейнерами единообразно, не зная разницы между ними.  
  
### Задание
Создайте еще 2 декоратора:  
Sugar - декоратор, добавляет сахар, увеличивая цену на 5  
Chocolate - декоратор, добавляет шоколад, увеличивая цену на 20  

Результат:  
Цена: 140, Кофе Американо, с молоком, с сахаром, с шоколадом
