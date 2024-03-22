### Задание 1. - Добавление товара в корзину

Вы создадите HTML форму, состоящую из одной кнопки добавления товара, на веб-странице и напишите обработчик на сервере.  

1. Откройте Visual Studio, откройте папку `C:\xampp\htdocs`
2. Создайте файл add_card.html, используя эммет `!` задайте html-структуру 
3. Создайте HTML форму на веб-странице, содержащую следующие элементы:
```
  <h1>Фирменный гамбургер от Бургер-Крик</h1>
  <p></p>

  Добавьте форму с method="POST" action="add.php"
  Добавьте скрытое поле с идентификатором <input type="hidden" name="id" value="101">
  Добавьте поле с названием товара name="name_product" и значением "Фирменный гамбургер"
  Внутри добавьте кнопку <button type="submit"> и текстом "Добавить в корзину" для отправки формы.
```
4. Напишите простой серверный скрипт `add.php` на PHP для обработки данных формы.  
В этом скрипте необходимо использовать сессии для хранения выбранных товаров на стороне клиента.
```
<?php
session_start();

if (isset($_POST['id'])) {
    $product_id = $_POST['id'];

    if (!isset($_SESSION['basket'])) {
        $_SESSION['basket'] = [];
    }

    if (isset($_SESSION['basket'][$product_id])) {
        $_SESSION['basket'][$product_id]['quantity']++;
    } else {
        $_SESSION['basket'][$product_id] = [
            'name' =>  $_POST['name_product'],
            'quantity' => 1
        ];
    }

    echo "Товар успешно добавлен в корзину!<br>
    (Всего ".$_SESSION['basket'][$product_id]['name']." в корзине ".strval($_SESSION['basket'][$product_id]['quantity']) . ")\n";

    echo "Данные сессии
    <pre>";
    echo "<pre>";
    var_dump($_SESSION['basket']);
    echo "</pre>";

}
?>
```

Протестируйте функционал добавления товара в корзину,   
проверяя сохранение товара 2 и более раз.

Запустите `Xamp Control \ Apache start` -> в браузере вызовите `localhost/add_card.html`
<hr>

### Задание 2. - Добавление классов на сайт

1. Скопируйте все файлы (и каталоги) из папки `BurgerKrig` в папку `C:\xampp\htdocs`
* Если у вас нет проекта `BurgerKrig` в каталоге пользователя, скачайте базовый проект:
```
В директории пользователя выполните - если проект уже был добавлен ранее
git pull

- если проекта еще нет
git clone https://github.com/Coopteh/BurgerKrig.git

cd BurgerKrig
```
2. Переименуйте файл `index.html` в `index.php` и добавьте php-вставку в самое начало файла
```
<?php 
	 include("./routers/Router.php");
	
	 $router = new Router();
	 $url = $_SERVER['REQUEST_URI'];

	 echo $router->route($url);

	 exit;
?>
```
3. Создайте в корне папки `C:\xampp\htdocs` файл `.htaccess`
```
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ /index.php
```
.htaccess — это локальный конфигурационный файл веб-сервера Apache, который позволяет управлять настройками сайта.   
в нем мы задали условия чтобы все запросы перенаправлялись в один файл с именем index.php

3. Вызовите в браузере `http://localhost/products` - это единственный маршрут реализованный нами в классах и через роутер  
4. Вам должны быть показаны описания 3 товаров без какой-либо красивой верстки.
<hr>

### Задание 3. - Добавление новых данных (картинки, описания, веса)

Теперь у нас отображаются товары, но не все данные, если посмотреть на страницу с версткой [http://localhost/products.html](http://localhost/products.html)  
- на ней есть для каждого товара дополнительно - картинка, описание, вес

Добавьте в файл `test_storage.php` дополнительные данные (в массив `$arrData`), например:
```
        ['id' => 1, 'name' => 'Гамбургер', 
        'description' => 'Котлета из мраморной говядины, салат айсберг, соус сильвер и барбекю, томат свежий, огурец консервированный, лук фри',
        'image' => "./img/image1.jpg",
        'weigth' => 240, 
        'price' => 355.00],
```
Запустите на выполнение и проверьте результат (массив) в консоли

* если хотите получить удобочитаемый формат (каждая пара ключ-значение на отдельной строке) в data.json  
используйте опцию JSON_PRETTY_PRINT для функции json_encode
```
    public function saveData($nameFile, $arr)
    {
        $json = json_encode($arr, JSON_PRETTY_PRINT);
```
