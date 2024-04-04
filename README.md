### Задание 1. - Класс работы с текстом

Необходимо научиться писать модульные тесты для разного вида классов.

1. В `Visual Studio Code` откройте `Документы \ php-is-211`    
2. Создайте файл `PersonaName.php` внутри папки `src` c классом `PersonaName`  
5. Создайте метод `firstUpper($name)` который формирует строку из первой заглавной и остальными строчными буквами  
- используйте функцию [ucfirst](https://www.php.net/manual/ru/function.ucfirst.php)
```
    static function mb_ucfirst($string) {
        $string = mb_strtoupper(mb_substr($string, 0, 1)) . mb_substr($string, 1);
        return $string;
    }
    public function firstUpper($name) {
        return PersonaName::mb_ucfirst($name);
    }
```
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

1. Создайте поля класса: `firstname, lastname, surname` (имя, фамилия, отчество)
2. Создайте конструктор для инициализации значений этих полей
3. Создайте метод `fio()`, который берет первые буквы каждого из полей имени и отчества
и добавляет, через пробел, к полю фамилии, формируя строку ФИО, вида: `Иванов П.С.`
4. Создайте новый тест `test_fio()` - в папке `Test` и подпапке `Unit` 
Добавьте проверку:
```
$obj2 = PersonaName('Иванов', 'Петр', 'Сергеевич');
$this->assertEquals( 'Иванов П.С.', $obj2->fio());
```


### Задание 3. - ФИО +

1. Измените метод `fio()` (используйте метод `firstUpper($name)` для преобразования) так, чтобы
выполнялась новая проверка для теста `test_fio()`:
```
$obj3 = PersonaName('иванов', 'пEТР', 'сергеевич');
$this->assertEquals( 'Иванов П.С.', $obj3->fio());
```
