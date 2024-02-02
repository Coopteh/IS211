# Паттерн "Приспособленец" (Flyweight)
применяет совместное использование для эффективной поддержки множества мелких объектов    
структурный паттерн  

**Назначение:**  
может использоваться для экономии памяти или других ресурсов,   
предоставляя общие объекты, разделяемые между множеством контекстов,   
вместо повторного создания одинаковых объектов.  

Рассмотрим пример
```
import random
import string

# Приспособленец (Flyweight)
class Robot:
    def __init__(self, name):
        self.name = name
        self.color = ''.join(random.choices(string.ascii_letters, k=4))
        self.height = random.randint(140, 200)  # в см
        self.weight = random.randint(50, 100)  # в кг

    def display(self):
        return f"Имя: {self.name}, Цвет: {self.color}, Высота: {self.height}, Вес: {self.weight}"


# Приспособленцы фабрики
class RobotFactory:
    robots = {}

    def get_robot(self, name):
        if name not in self.robots:
            self.robots[name] = Robot(name)
        return self.robots[name]

    def count_robots(self):
        return len(self.robots)
```
Использование:
```
def main():
    robot_factory = RobotFactory()
    names = ['Robot1', 'Robot2', 'Robot3', 'Robot4', 'Robot5', 'Robot1', 'Robot2']

    for name in names:
        robot = robot_factory.get_robot(name)
        print(robot.display())

    print(f"Всего создано уникальных роботов: {robot_factory.count_robots()}")


if __name__ == "__main__":
    main()
```
В этом примере:
- Robot представляет приспособленца (Flyweight),  
предоставляющего информацию о роботе, такую как имя, цвет, рост и вес.
  
Паттерн "Приспособленец" может использоваться для  
уменьшения использования памяти путем повторного использования общих объектов.

### Задание
на МКС потребовался робот "Fedor"  
- добавьте его имя в начало и конец списка names  
- убедитесь, что в обоих случаях (запроса робота) используется один и тот же экземпляр класса (одинаковые рост и вес)
