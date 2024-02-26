## Задача 9/1
Допишите реализацию функции invertCase(),   
которая инвертирует регистр каждого символа в переданной строке  
(ищите mb_strtoupper, mb_strtolower, mb_strpos, mb_strlen)
```
$str = 'ПрИвЕт!';
print_r( invertCase($str) ); // пРиВеТ!
```

## Задача 9/2
Реализуйте функцию getCustomDate(),  
которая принимает дату в формате timestamp и возвращает ее в формате 15/03/1985
```
print_r( getCustomDate(1532435204)."\n" ); // 24/07/2018
print_r( getCustomDate(532435204)."\n" );  // 15/11/1986
print_r( getCustomDate(5324352)."\n" );    // 03/03/1970
```
Подсказки
- используйте функцию date c параметром 'd/m/Y'
