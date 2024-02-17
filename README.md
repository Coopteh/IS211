## Задача 1
Напишите функцию getAgeDifference(),  
которая принимает два года рождения и возвращает строку с разницей в возрасте в виде  
The age difference is 11. Например:  
```
<?php

$actual = getAgeDifference(2001, 2018);
print_r($actual); // => The age difference is 17

$actual2 = getAgeDifference(2020, 2002);
print_r($actual2); // => The age difference is 18
```
Подсказки
```
В PHP есть функция abs(), которая возвращает модуль переданного числа. Например, abs(-12) вернёт 12.
```

## Задача 2
```
В PHP из языка Си перекочевала интересная функция sprintf(). Она создает строку на основе шаблона и данных:

<?php

 

$result = sprintf('Today is %s %d', 'February', 8);

print_r($result); // => Today is February 8

Первый аргумент в sprintf() — строка-шаблон. Кроме самого текста, в ней могут присутствовать специальные заполнители. Это «заглушки» для информации, которая передается следующими аргументами. %s означает «заглушка для строки», %d — для числа. Поэтому следующие два аргумента в нашем примере — строка и число.

Порядок и тип значений должны совпадать с порядком типом заглушек.

При выводе дат иногда требуется фиксировать количество цифр. Скажем, всегда писать нули перед числом, если число меньше 10. Здесь sprintf() позволяет решить эту задачу:

<?php

 

$result = sprintf('Today is %s %02d', 'February', 8);

print_r($result); // => Today is February 08

%02d — сделать две цифры и заполнить нулями оставшееся пространство. %03d — три цифры, и так далее:

<?php

 

$result = sprintf('Today is %s %04d', 'February', 8);

print_r($result); // => Today is February 0008
```

Задание

Реализуйте функцию getFormattedBirthday(), которая принимает на вход три параметра: день, месяц и год рождения.  
Она возвращает их строкой в отформатированном виде, например: 20-02-1953.
```
<?php

$result = getFormattedBirthday(20, 2, 1953);

print_r($result); // => 20-02-1953
```
День и месяц нужно форматировать так, чтобы при необходимости добавлялся 0 слева.  
Например, если в качестве месяца пришла цифра 7, то в выходной строке она должна быть представлена как 07.  

## Задача 3

Реализуйте функцию isLeapYear(), которая проверят год на високосность.  
Год будет високосным, если он кратен 400 или он одновременно кратен 4 и не кратен 100.  
Как видите, в определении уже заложена вся необходимая логика, осталось только переложить ее на код:  
```
  <?php

  isLeapYear(2018); // false

  isLeapYear(2017); // false

  isLeapYear(2016); // true
```
Подсказка

Посмотрите на распределение високосных годов в григорианском (https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%81%D0%BD%D1%8B%D0%B9_%D0%B3%D0%BE%D0%B4#%D0%93%D1%80%D0%B8%D0%B3%D0%BE%D1%80%D0%B8%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%B0%D0%BB%D0%B5%D0%BD%D0%B4%D0%B0%D1%80%D1%8C)[rfktylfht]
