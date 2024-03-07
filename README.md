### Задание - Класс хранения данных

Нужно разработать класс чтения и записи массива в файл, в json формате  

1. Создайте папку `BurgerKrig`
2. Создайте внутри папку `interfaces` и в ней файл `FileStorageInterface.php`  
Скопируйте интерфейс работы с файлами
```
interface FileStorageInterface {
     public function saveData($arr);
     public function loadData():array;
}
```
3. Создайте внутри `BurgerKrig` папку `services` и в ней файл `FileStorage.php`
класс FileStorage реализует интерфейс FileStorageInterface
- метод saveData($obj)    - принимает объект, переводит его сериализует его и сохраняет в файл, заданный константой NAME_FILE
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
