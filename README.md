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
print_r( joinNumbersFromRange(1, 1) );  // '1'
print_r( joinNumbersFromRange(2, 3) );  // '23'
print_r( joinNumbersFromRange(5, 10) ); // '5678910'
```
пройтись по всем числам диапазона и использовать конкатенацию для получения результирующей строки.
