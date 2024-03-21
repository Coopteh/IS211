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
