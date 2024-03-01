## Задача 12.1 Создание объектов, инкапсуляция 
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

