# Паттерн "Цепочка обязанностей" (Chain of responsibility)
поведенческий паттерн  
позволяет избежать привязки отправителя запроса к его получателю,  
предоставляя возможность обработать запрос нескольким объектам.  
Связывает объекты получатели в цепочку и передает запрос по цепочке, пока он не будет обработан

Рассмотрим пример
```

# Интерфейс
class IWorker():
    def set_next_worker(self, worker):
        pass

    def execute(self, command):
        pass

class Worker(IWorker):
    def __init__(self):
        self.__next_worker = None

    def set_next_worker(self, worker):
        self.__next_worker = worker
        return self

    def execute(self, command):
        if self.__next_worker is not None:
            return self.__next_worker.execute(command)
        return ''

class Designer(Worker):
    def execute(self, command):
        if command == "проектировать дом":
            return "Проектировщик выполнил команду: "+command
        else:
            return super().execute(command)

class Carpenter(Worker):
    def execute(self, command):
        if command == "класть кирпич":
            return "Плотник выполнил команду: "+command
        else:
            return super().execute(command)

class FinishWorker(Worker):
    def execute(self, command):
        if command == "клеить обои":
            return "Обойщик выполнил команду: "+command
        else:
            return super().execute(command)

def give_command(worker: IWorker, command: str):
    result = worker.execute(command)
    if result == '':
        print(command + ' - никто не умеет делать')
    else:
        print(result)

if __name__=='__main__':
    designer = Designer()
    carpenter = Carpenter()
    finish_worker = FinishWorker()

    designer.set_next_worker(carpenter).set_next_worker(finish_worker)

    give_command(designer, 'спроектировать дом')
    give_command(designer, 'класть кирпич')
    give_command(designer, 'клеить обои')

    give_command(designer, 'провести проводку')
```

В этом примере:
- IWorker - определяет общий интерфейс всех обработчиков
- Worker - определяет назначение последователя (сохраняя его в поле объекта)
и передачу выполнения последователю, если он определен
- Designer, Carpenter, FinishWorker - конкретные обработчики, которые  
либо обрабатывают запрос, либо передают его следующему обработчику в цепочке  
через родительский класс Worker
 
Паттерн "Цепочка обязанностей" позволяет передавать запросы последовательно по цепочке обработчиков до тех пор, пока запрос не будет обработан.

### Задание
- создайте класс директора Manager, который "обрабатывает документы"  
все команды посылайте через него  

Убедитесь, что несмотря на наличие директора, цепочка по-прежнему работает))
