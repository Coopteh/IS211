# Паттерн "Компоновщик" (Composite) 
компонует объекты в древовидные структуры для представления иерархий "часть - целое"
структурный паттерн  

**Назначение:**  
Паттерн "Компоновщик" описывает как можно применить рекурсивную композицию таким образом, что клиенты не придется проводить различие между простыми и составными объектами.

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
- есть иерархия классов Цвет - абстракция IColor, классы RedColor и BlueColor, представляющие конкретные реализации цветов.
- есть класс Shape, который представляет абстракцию, классы Square и Circle - конкретные реализации, каждая из которых использует одну из реализаций свойства (color) для применения цвета к форме.
- класс Shape - мост между своей реализацией класса фигур и использования свойства цвет из другой иерархии классов, посредством композиции.
  
### Задание
Создайте еще 3 класса:  
TwoCircle - простой узел, который рисует ' O   O '
Noise - простой узел, который рисует '   |   '
Mouth - простой узел, который рисует ' ~~~ '
добавьте узлы в контейнер picture и вызовите picture.draw()
