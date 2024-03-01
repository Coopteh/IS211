### Задача 12.1 Создание объектов, инкапсуляция 
1. Создайте или откройте в Visual Studio Code папку Документы/Php-IS-211
2. Создайте новый файл oop1.php
3. Создайте в нем новый класс Animal
```
<?php

class Animal {
     private string name;
     private int count;

     public function __construct(string name, int count) {
          ...
     }

     public function __toString() {
         ...
     }
}
```
Создайте экземпляр класса Animal и распечатайте объект через echo
```
obj = new Animal('корова', 4);
echo obj;
```

### Задача 12-2 Геттеры, сеттеры, наследование и полиморфизм
1. Создайте для класса Animal новое поле `private string $voice;`
2. Добавьте геттер и сеттер для поля `$voice`;
3. Добавьте метод `say()` который для Animal выводит `- без звука -`
4. Измените метод __toString() на вывод  
`"{$this->name}, имеет: {$this->count} ног, голос: {$this->voice} \n";`

6. Наследование - создайте 3 дочерних от Animal класса:
   Dog, Cow, Sparrow (воробей)
8. Создайте методы `say()` для каждого из 3 классов Dog, Cow, Sparrow
- для Dog метод `say()` выводит `Гав-гав`
- для Cow метод `say()` выводит `Му-у`
- для Sparrow метод `say()` выводит `Чик-чирик`

6. Создайте объекты классов Dog, Cow, Sparrow
- назначьте голос для каждого объекта через сеттер `setVoice()`
- вызовите для каждого объекта:
```
echo $obj;
echo $obj->say();
```
