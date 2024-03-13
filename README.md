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
создайте объект класса ProductTemplate и вызовите его метод getTemplate( $products );
присвойте переменной $template полученное значение

3. Верните значение $template из функции
```

Проверочный код - создайте скрипт `test_product.php`
```
$obj = new Product();
echo $obj->route('https://mysite.ru/products') ."\n";      // Вызван метод getAll() из класса Product'
```
