### Задание 1 - Проектирование диаграмм классов

1. Откройте по ссылке [Draw.io](https://draw.io) и выберите "Сохранять диаграмму" -> Этот компьютер  
2. Создайте диаграмму класса `Router` и диаграмму класса `Products` (с методами `get(id: int): string` и `getAll():string`)
3. Создайте класс FileStorage с методами `saveData(nameFile: string, arr: array)` и `loadData(nameFile: string): array`
4. Создайте класс ProductTemplate с методами `getTemplate(arr:array):string` расширяющий класс BaseTemplate c методом `getTemplate():string` 
5. Соедините классы и укажите по каким `url` будут происходить вызовы
6. Сохраните файл и сделайте скриншот для курсовой работы.

### Задание 2 - Создание шаблона продукта

Нужно разработать класс базовой разметки `BaseTemplate`

- Откройте папку с проектом папку `BurgerKrig`  
- Создайте внутри папку `templates` и в ней файл `BaseTemplate.php`   
- Скопируйте в файл класс с методом `getBaseTemplate()`, который возвращает базовую разметку html-страницы  
(внутри тегов `<body>` и `<title>` вставлены `%s` для добавления строки в шаблон и последующего использования функции `sprintf`)
```
class BaseTemplate {  
    public function getBaseTemplate() {
        $template = <<<END
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>%s</title>
        </head>
        <body>
            %s
        </body>
        </html>
        END;
        return $template;
    }
}
```
- Создайте внутри папки `templates` файл `ProductTemplate.php` с классом `ProductTemplate` и наследуйте его от `BaseTemplate.php`
- Добавьте в начало файла включение модуля `include ("BaseTemplate.php");`
- Реализуйте метод `getTemplate(arr:array):string`
```
Переменная $template получает базовый шаблон страницы от родителя, вызовом функции parent::getBaseTemplate();
В цикле (foreach) обойдите все элементы переданного простого массива `$arr`,
который содержит ассоциативные массивы с описаниями товаров сайта

Сформируйте строку со списком товаров
"<h1>". $item['name'] . ", ". $item['price'] ."</h1>"

Подставьте полученную строку со списком товаром ($str) в базовый шаблон страницы,
передав еще текст заголовка 'Список товаров',
используя функцию sprintf()

sprintf($template, 'Список товаров', $str);

Верните полученный результат - шаблон списка товаров
```

Создайте тестовый файл `test_template.php`
```
<?php
include ("./templates/ProductsTemplate.php");
include ("./services/FileStorage.php");

$store = new FileStorage();
$arrData = $store->loadData('data.json');

$templ = new ProductsTemplate();
echo $templ->getTemplate($arrData);
```
Если у вас нет файла `data.json`, тогда запустите на выполнение файл `test_storage.php`  
Запустите файл `test_template.php` - проверьте полученный результат:  
```
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Список товаров</title>
</head>
<body>
    <h1>Гамбургер, 450</h1><h1>Чизбургер, 360</h1><h1>Чикенбургер, 500</h1>
</body>
</html>
```

