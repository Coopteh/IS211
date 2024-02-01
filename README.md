# Паттерн "Фасад" (Facade) 
предоставляет унифицированный интерфейс вместо набора интерфейсов, который предоставляют подсистемы  
структурный паттерн  

**Назначение:**  
Разбиение на подсистемы облегчает проектирование сложной системы в целом.  
Общая цель всякого проектирование - свести к минимуму зависимость подсистем друг от друга и обмен информацией между ними.  
Один из способов решения этой задачи - введение объекта фасад, который предоставляет единый упрощенный интерфейс
к более сложным системным средствам.

Рассмотрим пример
```
# Подсистема компонентов
class CPU:
    def freeze(self):
        return "Раскрутим процессор"

    def jump(self, position):
        return f"Переход к регистру {position}"

    def execute(self):
        return "Выполнение"


class Memory:
    def load(self, position, data):
        return f"Загружаем из регистра {position} данные: {data}"


class HardDrive:
    def read(self, lba, size):
        return f"Читаем с сектора {lba} данные размером {size}"


# Фасад
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        result = [self.cpu.freeze(), self.memory.load("0x00", "boot"), self.cpu.jump("0x00"), self.cpu.execute()]
        return '\n'.join(result)
```
Использование:
```
# Использование
def main():
    computer = ComputerFacade()
    print(computer.start())


if __name__ == "__main__":
    main()
```
В этом примере:  
- CPU, Memory и HardDrive - подсистемы, с которыми взаимодействует фасад.  
- ComputerFacade - фасад, предоставляющий упрощенный интерфейс для взаимодействия с подсистемами.  
 
Паттерн "Фасад" позволяет скрыть сложность внутренних систем путем предоставления удобного высокоуровневого интерфейса.

### Задание
Задействуйте в методе start() класса ComputerFacade запуск чтения с жесткого диска (класс HardDrive, метод read)
