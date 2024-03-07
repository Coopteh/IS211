### Задание - Класс хранения данных

Нужно разработать класс (FileStorage - Файловое хранилище)  
чтения и записи массива с данными в файл, в json формате  

1. Создайте папку `BurgerKrig`
2. Создайте внутри папку `interfaces` и в ней файл `FileStorageInterface.php`  
Скопируйте интерфейс работы с файлами
```
interface FileStorageInterface
{
    public function saveData($nameFile, $arr);
    public function loadData($nameFile): ?array;
}
```
3. Создайте внутри `BurgerKrig` папку `services` и в ней файл `FileStorage.php`
класс FileStorage реализует интерфейс FileStorageInterface (добавьте включение интерфейса через `include`)
- метод `saveData($nameFile, $arr)`    - принимает массив (`$arr`)
и переводит его в строку формата json - вызовом функции:  
[json_encode](https://www.php.net/manual/ru/function.json-encode.php) — Возвращает JSON-представление данных (строку)  
сохраняет в файл, заданный аргументом `$nameFile`  
```
для записи в файл используейте
$handle = fopen($nameFile, "w");
опция "w" - режим записи, переписывает все данные в файле
см. также функции fwrite(), fclose()
```

- метод `loadData($nameFile)` - загружает строки данных из файла (`$nameFile`) и переводит их в массив, вызовом функции
[json_decode](https://www.php.net/manual/ru/function.json-decode.php) — Декодирует строку JSON   
```
для чтения из файла используйте
$handle = fopen($nameFile, "r");
опция "r" - режим чтения данных из файла
см. также функции fread(), fclose()
```

**Проверочный код**   
- поместите его в файл `test_code.php` в корень папки `BurgerKrig`
- подключите класс работы с файловым хранилищем `include ("./services/FileStorage.php");`
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
