# Паттерн Мост (Bridge)
Структурный паттерн  

**Назначение:**  
Паттерн "Мост" позволяет отделить абстракцию от её реализации, 
чтобы оба могли изменяться независимо друг от друга. 
Это улучшает расширяемость системы.

**Обоснование паттерна**  
В случае когда некоторая абстракция может иметь несколько реализаций используют наследование. 
Абстратный класс определяет интерфейс (спецификацию методов для работы с группой классов), 
а конкретные подклассы (наследники) по-разному его реализуют.

Мост - класс (реализации), который посредством композиции принимает некоторую иерархию классов (свойств).    
Рассмотрим пример
```
Есть реализация иерархии классов цвет

# Абстракция свойства
class IColor:
    def apply_color(self):
        pass
 
class RedColor(IColor):
    def apply_color(self):
        return "red"
 
class BlueColor(IColor):
    def apply_color(self):
        return "blue"

# Абстракция реализатора
class Shape:
    def __init__(self, color):
        self.color = color
 
    def apply_color(self):
        pass
 
# Конкретные реализации
class Square(Shape):
    def apply_color(self):
        return f"Используется {self.color.apply_color()} цвет - для КВАДРАТА"
 
class Circle(Shape):
    def apply_color(self):
        return f"Используется {self.color.apply_color()} цвет - для КРУГА"
```
вызов экземляров классов:
```
def main():
    red_square = Square(RedColor())
    blue_circle = Circle(BlueColor())
    print(red_square.apply_color())  
    print(blue_circle.apply_color())
 
if __name__ == "__main__":
    main()
```
В этом примере:  
- есть иерархия классов Цвет - абстракция IColor, классы RedColor и BlueColor, представляющие конкретные реализации цветов.
- есть класс Shape, который представляет абстракцию, классы Square и Circle - конкретные реализации, каждая из которых использует одну из реализаций свойства (color) для применения цвета к форме.
- класс Shape - мост между своей реализацией класса фигур и использования свойства цвет из другой иерархии классов, посредством композиции.
  
