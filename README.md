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
```
    $sql = "INSERT INTO user (email, first_name, last_name, age, date_created)
    VALUES ('iTom@mail.ru', 'Тимофей', 'Иванов', 15, '2024-04-08')";
    $conn->exec($sql);

    $conn->exec("INSERT INTO user (email, first_name, last_name, age, date_created)
    VALUES ('iTom2@mail.ru', 'Тимофей2', 'Иванов', 16, '2024-04-08')");

    $conn->exec("INSERT INTO user (email, first_name, last_name, age, date_created)
    VALUES ('petr@mail.ru', 'Петр', 'Петров', 17, '2024-04-08')");
```
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
   
### Задание 4. - Табличное представление данных

Используя шаблоны [Bootstrap](https://getbootstrap.com) выведите данные для просмотра в таблицу  
1. Сначала оформите вывод в простую таблицу (тегами table, tr, td)
2. Найдите в созданном ранее проекте класс Basetemplate и скопируйте метод `getBaseTemplate` в файл `sql.php`
3. Используйте этот метод для получения базового шаблона страницы и добавьте сверстанную таблицу из переменной `$html`  
используя функцию `sprintf()`:
```
$template =sprintf( getBaseTemplate(), $html );
```

