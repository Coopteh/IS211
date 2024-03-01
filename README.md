### Задача 1 Абстрактные классы
1. Создайте или откройте в Visual Studio Code папку Документы/Php-IS-211
2. Создайте новый файл abstract.php
3. Создайте в нем новый абстрактный класс Transport, содержащий:
- Абстрактный метод start(), описывающий начало движения транспортного средства.
- Абстрактный метод stop(), описывающий остановку транспортного средства.
- Метод honk(), с реализацией по умолчанию, который будет издавать звук сигнала.
```
<?php

abstract class Transport {
    abstract public function start();
    abstract public function stop();
 
    public function honk() {
        return "Beep beep!";
    }
}
```
4. Создайте классы, расширяющие абстрактный класс Transport, например:
 - Car (автомобиль) с собственными реализациями методов start() и stop().
 - Bicycle (велосипед) с собственными реализациями методов start() и stop().

так чтобы работала реализация
```
$car = new Car();
echo $car->start(); // Автомобиль завелся и тронулся с места
echo $car->honk();  // Би-би-ип
echo $car->stop(); // Автомобиль остановился

$bicycle = new Bicycle();
echo $bicycle->start(); // Велосипедист крутит педали
echo $bicycle->honk();  // Дзынь-дзынь
echo $bicycle->stop(); // Велосипедист жмет на тормоза
```

### Задача 2 Интерфейсы
1. Создайте новый файл interface.php
2. Создайте в нем интерфейс TransportInterface, содержащий следующие объявления методов:
   - start(), который описывает начало движения транспортного средства.
   - stop(), который описывает остановку транспортного средства.
```
interface VehicleInterface {
    public function start();
    public function stop();
}
```   
2. Создайте классы, реализующие интерфейс VehicleInterface, например:
   - Car, который реализует методы start() и stop().
   - Bicycle, который реализует методы start() и stop().
   
3. Дополнительное задание: Добавьте дополнительные методы или свойства в интерфейс и реализующие классы, чтобы продемонстрировать применение интерфейсов для унификации работы с различными типами транспортных средств.

**Пример:**

interface VehicleInterface {
    public function start();
    public function stop();
}

class Car implements VehicleInterface {
    public function start() {
        return "Car started.";
    }

    public function stop() {
        return "Car stopped.";
    }
}

class Bicycle implements VehicleInterface {
    public function start() {
        return "Bicycle started pedaling.";
    }

    public function stop() {
        return "Bicycle stopped pedaling.";
    }
}

// Пример использования:
$car = new Car();
echo $car->start(); // Вывод: Car started.
echo $car->stop(); // Вывод: Car stopped.

$bicycle = new Bicycle();
echo $bicycle->start(); // Вывод: Bicycle started pedaling.
echo $bicycle->stop(); // Вывод: Bicycle stopped pedaling.
