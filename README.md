## Задача 10/1
Реализуйте функцию reverse(), 
которая переворачивает цифры в переданном числе:
```
use function App\Number\reverse;

print_r( reverse(13) . "\n"); // 31
print_r( reverse(-123) . "\n"); // -321

```
Не забудьте задать тип входного и выходного аргумента.

Подсказки
```
Переворот строки  https://www.php.net/manual/ru/function.strrev.php  
Одно из решений этой задачи опирается на явное преобразование типов

strval($v)    - преобразует в строку
intval($v)    - преобразует в целое число
strrev($v)    - переворачивает строку задом наперед
abs($v)       - модуль числа
```

