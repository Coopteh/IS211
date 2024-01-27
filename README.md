# Описание паттерна проектирования Singleton
Класс, реализующий паттерн Одиночка (Singleton)
```
class Singleton:
    # Приватная переменная для хранения единственного экземпляра
    _instance = None

    def __new__(cls, data):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"data = {self.data}"

# Использование паттерна Одиночка
obj1 = Singleton('Один')
obj2 = Singleton("Второй")
obj3 = Singleton("Третий")
print(obj1)
print(obj2)
print(obj3)
print(obj3 is obj1)
```
