### Задание 1 - Серверный скрипт обработки строк

1. Откройте Visual Studio, откройте папку `C:\xampp\htdocs`
2. Откройте файл index.php, используя эммет `!` задайте html-структуру 
3. в секцию `body` запишите преобразование строки  
`$str = 'Имя|Фамилия|Отчество|Год рождения|Рост|Вес|Номер кредитной карты';`
в строку   
`'Имя, Фамилия, Отчество, Год рождения, Рост, Вес, Номер кредитной карты';`

Используйте функции:  
[explode](https://www.php.net/manual/ru/function.explode.php) — Разбивает строку разделителем   
[implode](https://www.php.net/manual/ru/function.implode.php) — Объединяет элементы массива в строку  
echo   - для вывода строки   

Запустите `Xamp Control` и в нем запустите `Apache` - откройте в браузере `localhost`  




### Задание 2 - Работа с сериализацией и десериализацией объектов на PHP

Нужно создать классы, которые могут быть сериализованы и десериализованы в PHP.  

Они будут использовать встроенные функции PHP для сериализации объектов в строку и восстановления объекта из строки.
Читайте подробнее: 
[serialize](https://www.php.net/manual/ru/function.serialize.php),    
[unserialize](https://www.php.net/manual/ru/function.unserialize.php)   

**Шаги**

1. Создайте класс Student, содержащий свойства об объекте студента (например, имя `$name`, возраст `$age`, курс `$course`)

2. Реализуйте методы serialize() и unserialize() в классе Student:
   - Метод serialize() должен преобразовывать объект класса Student в строку.   
   `serialize([$this->name, $this->age, $this->course]);`
   - Метод unserialize() должен извлекать объект класса Student из строки и восстанавливать его.    
    `[$this->name, $this->age, $this->course] = unserialize($data);`

3. Создайте объект класса Student, заполните его данными и протестируйте сериализацию и десериализацию объекта.
```
// Создание объекта и сериализация
$student = new Student("Андрей", 18, "ИС-211");
$serializedData = $student->serialize();

// Десериализация объекта
$restoredStudent = new Student("", 0, "");
$restoredStudent->unserialize($serializedData);

// Проверка десериализованного объекта
echo "Восстановленный студент: Имя - {$restoredStudent->name}, Возраст - {$restoredStudent->age}, Курс - {$restoredStudent->course}";
```

Это задание показывает как сохранять и восстанавливать состояние объекта (его поля с данными)
с использованием встроенных функций PHP сериализации и десериализации объекта (перевода его в строку и обратно).  

### Задание 3 - Работа с файлами

Скопируйте интерфейс работы с файлами
```
interface FileStorageInterface {
     public function saveData($obj);
     public function loadData():mixed;
}
```
Создайте класс FileStorage реализующий интерфейс FileStorageInterface

- метод saveData($obj)    - принимает объект, сериализует его и сохраняет в файл, заданный константой NAME_FILE
```
const NAME_FILE = 'data.txt';
```
Шаги:  
Сериализуем [serialize](https://www.php.net/manual/ru/function.serialize.php),    
Пишем в файл полученную строку [file_put_contents](https://www.php.net/manual/ru/function.file-put-contents)  

- метод loadData()      - загружает строку данных из файла и десериализует ее в объект
Шаги:  
Считываем из файла строку с данными [file_get_contents](https://www.php.net/manual/ru/function.file-get-contents)  
Десериализуем [unserialize](https://www.php.net/manual/ru/function.unserialize.php),    

Проверочный код
```
$store= new FileStorage();
$store->saveData(new Student("Андрей", 18, "ИС-211"));
$student = $store->loadData();
var_dump($student);
```
Откройте (в Проводнике) файл `data.txt` и посмотрите что в нем записано?  
