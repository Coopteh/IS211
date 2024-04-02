### Задание 1. - Модульные тесты

Необходимо настроить модульные тесты, научиться их писать и запускать.

Откройте (либо создайте, если нет такой папки) php-is-211   
Запустите в ней (через Проводник, в адресной строке) консоль `cmd`  
В консоле запустите  
`composer init` - установка менеджера зависимостей  
`composer require phpunit/phpunit` - установка компонента запуска модульных тестов phpunit  
Создайте папку и подпапку в ней `Tests \ Unit`  
Отредактируйте `composer.json`  
```
    "autoload": {
        "psr-4": {
            "Project\\": "src/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Test\\": "Test/"
        }
    },
```
Запустите, чтобы изменения `composer.json` вступили в силу  
`composer install`  

**Создание класса Circle**
Создайте папку `src` и с ней файл `src/Circle.php`  
Напишите класс Circle, который (в конструкторе) при создании принимает аргумент `radius`  
имеет поле `$radius` и метод `area()`, который вычисляет площадь круга (3.14 * $this->radius * $this->radius)  

**Создание модульного теста CircleTest**  
В папке `Tests \ Unit` создайте файл `CircleTest.php`
```
<?php 
namespace App\Test\Unit;

use PHPUnit\Framework\TestCase;
use Project\Circle;

class CircleTest extends TestCase {

    public function test_area() {
        $obj = new Circle(10);
        $this->assertEquals( 314, $obj->area());
    }
}
```
метод `test_area()` создает класс Circle с радиусом = 10 и проверяет правильность расчета площади:  
должно быть получено значение 314 (3.14 *10 *10) - эталонное значение (314) сравнивается с вычисляемым методом класса  

**Запуск тестов**  
Запустите модульные тесты из папки `Tests` выполнив в консоле:  
```
vendor/bin/phpunit Test/
```
