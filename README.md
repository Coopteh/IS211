### Задание 1. - Класс работы с текстом

Необходимо научиться писать модульные тесты для разного вида классов.

1. В `Visual Studio Code` откройте `Документы \ php-is-211`    
2. Создайте файл `PersonaName.php` внутри него класс `PersonaName`  
5. Создайте метод `firstUpper($name)` который формирует строку из первой заглавной и остальными строчными буквами  
- используйте функцию [ucfirst](https://www.php.net/manual/ru/function.ucfirst.php)
6. Создайте тест `test_firstUpper` - в папке `Test` и подпапке `Unit` новый файл `PersonaNameTest.php` и соответствующий класс `PersonaNameTest`  
Добавьте проверку:
```
$obj = PersonaName();
$this->assertEquals( 'Иванов', $obj->firstUpper('иванов'));
```
7. Запустите модульные тесты из папки `Tests` выполнив в консоле:  
```
vendor/bin/phpunit Tests/
```
8. Измените метод `firstUpper($name)`, чтобы выполнялась проверка
```
$this->assertEquals( 'Иванов', $obj->firstUpper('ИВАНОВ'));
```

### Задание 2. - ФИО

1. Создайте поля класса: `firstName, lastName, surname`
2. Создайте конструктор для инициализации значений этих полей
   
