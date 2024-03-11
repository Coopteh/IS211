### Задание 1 - Проектирование диаграмм классов

1. Откройте по ссылке [Draw.io](https://draw.io) и выберите "Сохранять диаграмму" -> Этот компьютер  
2. Создайте диаграмму класса `Router` и диаграмму класса `Products` (с методами `get(id: int): string` и `getAll():string`)
3. Создайте класс FileStorage с методами `saveData(nameFile: string, arr: array)` и `loadData(nameFile: string): array`
4. Создайте класс ProductTemplate с методами `getTemplate(arr:array):string` расширяющий класс BaseTemplate c методом `getTemplate():string` 
5. Соедините классы и укажите по каким `url` будут происходить вызовы
6. Сохраните файл и сделайте скриншот для курсовой работы.

### Задание 2 - Создание шаблона продукта

Нужно разработать класс базовой разметки `BaseTemplate`

- Откройте папку с проектом папку BurgerKrig  
- Создайте внутри папку templates и в ней файл `BaseTemplate.php`   
- Скопируйте базовую разметку html-страницы (! эммет если файл имеет расширение .html)  
```
внутрь тега `<body>` вставьте `%s` для добавления строки в шаблон
```
- Наследуйте `ProductTemplate.php` от `BaseTemplate.php`
- Добавьте в метод `getTemplate(arr:array):string` вызов родительского метода `getTemplate():string`  
- и подстановки разметки в эту строку  
