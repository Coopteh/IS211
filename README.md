### Задание 1. - Модульные тесты

Необходимо.

Откройте (либо создайте, если нет такой папки) php-is-211 
cmd
composer init
composer require phpunit/phpunit
Tests \ Unit
composer.json
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
composer install
src/Circle
radius
area

CircleTest.php

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
