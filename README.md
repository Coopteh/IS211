### Задание 1. - Модульное тестирование граничных значений классов эквивалентности

Откройте `Visual Studio Code` в ней папку `php-is-211`   
и создайте в нем новый файл `DiscountCard.php` в подпапке `src`
1. Напишите класс `DiscountCard` (скидочная карта) и метод `getPercent()` в нем, который:
```
Считает процент скидки
0- до 1000 - 0%
от 1000 (включительно) - до 3000 3%
от 3000 (включительно) - 5000 5%
```
2. Напишите модульный тест `test_DiscountCard.php` в подпапке `tests\Unit` для проверки граничных значений  
 * определите классы эквивалентности  
 * определите границы диапазонов  
 * создайте 3 теста для границ (на самой, +1 значение, -1 значение) для каждого класса эквивалентности 
``` 
<?php 
namespace Test\Unit;

use PHPUnit\Framework\TestCase;
use Project\DiscountCard;

class TestDiscountCard extends TestCase {
    public function test_boundary() {

    }
}
```
Запустите модульные тесты из папки Tests выполнив в консоле:  
`vendor/bin/phpunit Tests/`   
Установка и настройка phpUnit - [по ссылке](https://github.com/Coopteh/IS211/tree/php-code-25-begin-unit-test)   

