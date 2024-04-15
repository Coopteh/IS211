### Задание 1. - Создание базы данных проекта BurgerKrig

1. Создайте новую пустую базу данных `burgerkrig` в MySQL.  
Для этого нужно воспользоваться phpMyAdmin (`localhost/phpmyadmin/`) включить `Xampp Control Panel \ Apache + mySql`  
2. В новой базе создайте таблицу `product` (продукция) со следующими полями, типами данных и ограничениями:
```
id — int, auto_increment, primary_key
name — varchar(120), not null, unique
description — text
image — varchar(100)
weigth — float
price — float, not null
created — datetime
updated — datetime
```
3. Cоздайте таблицу `order` (заказ) со следующими полями, типами данных и ограничениями:
```
id — int, auto_increment, primary_key
fio — varchar(120), not null
address — text
phone — varchar(15)
sum — float, not null
created — datetime
```
4. Cоздайте таблицу `order_item` (позиции заказа) со следующими полями, типами данных и ограничениями:
```
id — int, auto_increment, primary_key
order_id — int, not null
product_id — int, not null
count — int, not null 
price — float, not null
sum — float, not null
```
<hr>

Задание 2. Заполнение данными таблицы product

1. Включите `Xampp Control Panel \ Apache + mySql`  
2. Откройте в браузере `localhost` и страницу Каталога
3. Откройте в VSCode `c:\xampp\htdocs` и файл `sql.php`
4. Откройте phpMyAdmin (`localhost/phpmyadmin/`) и добавьте 3 запроса на вставку данных (INSERT INTO)
из каталога продукции в браузере в таблицу `product`

