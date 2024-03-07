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
- метод `saveData($nameFile, $arr)`    - принимает массив (`$arr`) вида:
```
[
['id'=> 1, 'name'=> 'Гамбургер','price'=> 450.00],
['id'=> 2, 'name'=> 'Чизбургер','price'=> 360.00],
['id'=> 3, 'name'=> 'Чикенбургер','price'=> 500.00],
]  
```
переводит его в строку формата json - вызовом функции
[json_encode](https://www.php.net/manual/ru/function.json-encode.php) — Возвращает JSON-представление данных (строку)  
его и сохраняет в файл, заданный аргументом `$nameFile`  
```
для записи в файл используейте
$handle = fopen($nameFile, "a");
опция "a" - добавляет данные в конец файла, добавляя их
```

- метод `loadData($nameFile)` - загружает строки данных из файла (`$nameFile`) и переводит их в массив, вызовом функции
[json_decode](https://www.php.net/manual/ru/function.json-decode.php) — Декодирует строку JSON   

Проверочный код
```
$store= new FileStorage();
$arrData = [
  ['id'=> 1, 'name'=> 'Гамбургер','price'=> 450.00],
  ['id'=> 2, 'name'=> 'Чизбургер','price'=> 360.00],
  ['id'=> 3, 'name'=> 'Чикенбургер','price'=> 500.00],
];
$store->saveData('data.json', $arrData);
```
Откройте (в Проводнике, Блокнотом) файл `data.json` и посмотрите что в нем записано?  
```
$arrData = $store->loadData('data.json');
var_dump($arrData);
```
Проверьте, что массив считан верно.  
