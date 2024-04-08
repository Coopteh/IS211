### Задание 1. - Создание базы данных

Создайте новую пустую базу данных `mydb` в MySQL.  
Для этого нужно воспользоваться phpMyAdmin (`localhost/phpmyadmin/`)  
`Xampp \ Apache + mySql`  
В новой базе создайте таблицу `Users` (пользователи) со следующими полями и типами данных соответственно:
```
id — int auto increment;
email — varchar(120);
first_name (имя) — varchar(100); 
last_name (фамилия) — varchar(100); 
age (возраст) — int; 
date_created (дата добавления) — datetime.
```

### Задание 2. - Работа с SQL - вставка данных

1. Откройте папку `c:\xampp\htdocs` и создайте новый файл `sql.php`
2. Установите в нем подключение к базе данных `mydb` средствами [PDO](https://www.php.net/manual/ru/book.pdo.php)  
3. Добавьте 3 записи в таблицу `Users`
4. Выполните скрипт `sql.php` через браузер `localhost/sql.php`

### Задание 3. - Работа с SQL - просмотр данных

1. Закомментируйте запрос на добавление данных
2. Добавьте запрос на выборку данных `SELECT`
3. Получите данные методом `fetch` из таблицы `Users` и выведите их в браузер
```
    $sql = "SELECT * FROM user";
    $result = $conn->query($sql);
    while($row = $result->fetch()) {
        // обработка строк
        echo "<pre>";
        echo "id = {$row['id']}, 
         имя и фамилия = {$row['first_name']} {$row['last_name']}, 
         возраст = {$row['age']}, 
         емайл = {$row['email']}";
        echo "</pre>";
    }
```
   
### Задание 4. - PDO работа с базой данных

Необходимо научиться добавлять, удалять, изменять и получать данные из БД при помощи PDO, а также работать с SQL-запросами средствами PDO.

Что нужно сделать
Создайте базу данных и таблицу товаров в ней.   
Реализуйте HTML-форму для добавления и изменения товаров, а также таблицу со списком всех товаров на этой же странице с кнопкой удаления напротив каждой записи.  

Создайте PHP-файл User.php, внутри него класс User. В классе User объявите поле $connection и в конструкторе класса инициализируйте подключение к вашей базе данных (указав имя хоста, логин, пароль и имя базы) с помощью PDO. Сохраните подключение в поле $connection. Данное подключение будет использоваться во всех последующих методах класса User.
Опишите метод create для класса User. В качестве входящего параметра он должен принимать ассоциативный массив с полями, необходимыми для добавления записи в таблицу Users. Метод должен выполнять вставку новой записи в таблицу Users с помощью PDO. Используйте SQL-запрос INSERT.
Опишите метод update для класса User. В качестве входящего параметра он должен принимать ассоциативный массив с полями, необходимыми для добавления записи в таблицу Users, а также id записи. Метод должен выполнять обновление существующей записи в таблице Users с помощью PDO. Используйте SQL-запрос UPDATE.
Опишите метод delete для класса User. В качестве входящего параметра он должен принимать id записи. Метод должен выполнять удаление существующей записи из таблицы Users с помощью PDO. Используйте SQL-запрос DELETE.
Опишите метод list для класса User. Он не принимает никаких параметров, а выводит все записи таблицы Users. Используйте PDO и запрос SELECT.
Создайте новый файл index.php и подключите к нему User.php.
Реализуйте вёрстку таблицы для вывода списка пользователей. Каждая строка таблицы должна соответствовать одной записи из базы данных. Все поля выводите в контролах input text. Добавьте колонку справа с кнопками edit (для сохранения изменённой записи) и delete (для удаления). Чтобы динамически вывести все записи, используйте метод list класса User и цикл foreach. Поместите код в начало файла index.php.
Под таблицей реализуйте форму для добавления пользователя.
После кода формы реализуйте серверную логику обработки действий по добавлению, изменению и удалению записи на PHP (отделите PHP-код тегами <?php ?>). 
Ваша форма, а также ссылки кнопок должны вести на файл index.php.
В зависимости от выбранного действия вызовите соответствующий метод класса User (create, update, delete). 

