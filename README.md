### Задание 1 - разработка класса Product

Скачайте базовый проект:
```
В директории пользователя выполните
- если проект уже был добавлен ранее
git pull

- если проекта еще нет
git clone https://github.com/Coopteh/BurgerKrig.git

cd BurgerKrig
```
Нужно реализовать метод getAll класса `Product`  
Откройте в Visual Studio Code папку с проектом `BurgerKrig`    
```
Реализуйте метод getAll():string
1. Загрузите данные в $products
создайте объект класса FileStorage и вызовите его метод loadData('data.json')
присвойте переменной $products полученное значение

2. Загрузите шаблон, передав ему загруженные данные
создайте объект класса ProductsTemplate и вызовите его метод getTemplate( $products );
присвойте переменной $template полученное значение

3. Верните значение $template из функции
```

Проверочный код - создайте скрипт `test_product.php`
```
include("./routers/Router.php");

$obj = new Router();
echo $obj->route('https://mysite.ru/products') ."\n";      // Вызван метод getAll() из класса Product'
```

На экран должно быть выведено
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
<hr>
### Задание 2 - Product (получение одного товара)

Реализуйте метод get(int $id):string класса Product  

