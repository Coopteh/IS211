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
echo $obj->route('https://mysite.ru/products') ."\n";      // должен быть вызван метод getAll() класса Product'
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

Создайте новый шаблон в ProductsTemplate - метод `getPageTemplate( $product )`  
он будет отображать страницу отдельного товара (с другой, отличной разметкой)   
```
скопируйте метод  getTemplate(array $arr): string
и назовите его  getPageTemplate(array $arr): string

код метода
        $template = parent::getBaseTemplate();
        $str= "<h1>". $arr['name'] . ", ". $arr['price'] ."</h1>";
        $resultTemplate = sprintf($template, 'Страница товара', $str);
        return $resultTemplate;
```
Реализуйте метод `get(int $id):string` класса Product   
```
Скопируйте содержимое метода getyAll()  

после присвоения $products возвращаемым значением из метода loadData('data.json')  
добавьте поиск значения $id в массиве $products:  

- используйте цикл foreach - чтобы пройтись по всем записям - отдельным массивам товаров  
и для каждого элемента проверьте есть ли $id в массиве
if ($product['id'] == $id) { .. }

Если $id найден, тогда:  
- возвращаете шаблон страницы товара:  
Создайте объект класса ProductsTemplate и вызовите его метод getPageTemplate( $product );  
Присвойте переменной $template полученное значение  
Верните значение $template из функции  

Если цикл завершился, значит $id не был найден
- верните код 404 ошибки  
    return '404';
```
Проверочный код - допишите в скрипт `test_product.php`
```
echo $obj->route('https://mysite.ru/products/1') ."\n";      // должен быть вызван метод get(1) класса Product
echo $obj->route('https://mysite.ru/products/100') ."\n";      // 404
```
На экран должно быть выведено
```
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Страница товара</title>
</head>
<body>
    <h1>Гамбургер, 450</h1>
</body>
</html>
404
```
