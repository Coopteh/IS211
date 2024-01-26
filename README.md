# Задание
Дана функция вычисляющая n! - факториал числа
```
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```
Напишите модульные тесты test\factorial_test.py  
проверяющие факториалы чисел:  
```
0! = 1
1! = 1
5! = 120
10! = 3628800
```
### Дополнительно 
Напишите проверку на неправильно введенное число (отрицательное):   
factorial(-1)  
Должно выпасть исключение ValueError  
его можно проверить с помощью self.assertRaises(..)   
реализуйте проверку исключения   
