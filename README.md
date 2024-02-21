## Задача 1
Модифицируйте функцию printNumbers() так, чтобы она выводила числа в обратном порядке.  
```
function printNumbers($firstNumber)
{

}
```
Для этого нужно идти от верхней границы к нижней.   
То есть, счетчик должен быть инициализирован максимальным значением, а в теле цикла его нужно уменьшать до нижней границы:
```
printNumbers(4);
// => 4
// => 3
// => 2
// => 1
// => finished!
```

## Задача 2

Реализуйте функцию joinNumbersFromRange(), 
которая объединяет все числа из диапазона в строку:
```
print_r( joinNumbersFromRange(1, 1) . "\n");  // '1'
print_r( joinNumbersFromRange(2, 3) . "\n");  // '23'
print_r( joinNumbersFromRange(5, 10) . "\n"); // '5678910'
```
пройтись по всем числам диапазона и использовать конкатенацию для получения результирующей строки.

## Задача 3

Реализуйте функцию-предикат isArgumentsForSubstrCorrect(), которая принимает три аргумента:
```
    Строку
    Индекс, с которого начинать извлечение
    Длину извлекаемой подстроки
```
```
function isArgumentsForSubstrCorrect($str, $ind, $length)
{

}
```
Не всегда значения, которые передаются в функцию, бывают корректными. Поэтому функция возвращает false, если хотя бы одно из условий истинно:
```
    Отрицательная длина извлекаемой подстроки
    Отрицательный заданный индекс
    Заданный индекс выходит за границу всей строки
    Длина подстроки в сумме с заданным индексом выходит за границу всей строки
```
В ином случае функция возвращает true.
Не забывайте, что индексы начинаются с 0, поэтому индекс последнего элемента — это «длина строки минус 1»:
```
$str = 'Sansa Stark';
echo isArgumentsForSubstrCorrect($str, -1, 3) . "\n";  // false
echo isArgumentsForSubstrCorrect($str, 4, 100) . "\n"; // false
echo isArgumentsForSubstrCorrect($str, 10, 10) . "\n"; // false
echo isArgumentsForSubstrCorrect($str, 11, 1) . "\n";  // false
echo isArgumentsForSubstrCorrect($str, 3, 3) . "\n";   // true
echo isArgumentsForSubstrCorrect($str, 0, 5) . "\n";   // true
```
