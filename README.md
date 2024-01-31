# Паттерн "Декоратор" (Composite) 
динамически добавляет объекту новые обязанности
структурный паттерн  

**Назначение:**  
Иногда нужно добавить новые обязанности объекту, а не классу в целом. То есть сделать это динамически, а не статически.

Рассмотрим пример
```
class Graphic:
    def draw(self):
        pass

# Лист (терминальный узел)
class Line(Graphic):
    def draw(self):
        print("-------")

class Circle(Graphic):
    def draw(self):
        print(" O     ")


# Контейнер (узел, содержащий потомков)
class Picture(Graphic):
    def __init__(self):
        self.children = []

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("Draw a picture:")
        for child in self.children:
            child.draw()
```
Использование:
```
def main():
    line = Line()
    circle = Circle()
    picture = Picture()
    picture.add(line)
    picture.add(circle)
    picture.add(line)
    picture.draw()


if __name__ == "__main__":
    main()
```
В этом примере:
- Graphic - абстрактный класс или интерфейс, который представляет как листья (терминальные узлы), так и контейнеры (узлы, содержащие потомков).  
- Line и Circle - простые листья, т.е. терминальные узлы.  
- Picture - контейнер, узел, способный хранить другие узлы в виде потомков.  
- Метод draw в каждом классе вызывает метод draw для всех своих потомков.  
 
Такой подход позволяет клиентскому коду работать с отдельными объектами и их контейнерами единообразно, не зная разницы между ними.
  
### Задание
Создайте еще 3 класса:  
TwoCircle - простой узел, который рисует ' O   O '  
Noise - простой узел, который рисует '   |   '  
Mouth - простой узел, который рисует ' ~~~ '  
добавьте узлы в контейнер picture и вызовите picture.draw()  
