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

### Задание 5. - Форма ввода для изменения данных

1. Добавим формы ввода для каждой записи в таблице
```
        // обработка строк
        $html .= "<tr>";
        // Добавим форму ввода
        $html .= "<form method='POST'>";
        // Добавим поля ввода
        $html .= "<td>{$row['id']}
          <input type='hidden' name='id' value='{$row['id']}'>
        </td> 
        <td>
          <input type='text' name='first_name' value='{$row['first_name']}'>
          <input type='text' name='last_name' value='{$row['last_name']}'>
        </td>
        <td><input type='text' name='age' value='{$row['age']}'></td>
        <td><input type='text' name='email' value='{$row['email']}'></td>";
        
         // Добавим кнопку Изменить
        $html .= "<td><button type='submit'>Изменить</button></td>";
        $html .= "</form>";
        
        $html .= "</tr>";
```
2. Обработаем данные формы, добавив после создания объекта PDO, следующий код:
```
    // Обработаем полученные данные - запрос на Изменение
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $id        = $_POST["id"];
        $first_name= $_POST["first_name"];
        $last_name = $_POST["last_name"];
        $age       = $_POST["age"];
        $email     = $_POST["email"];
    
        // Составим запрос
        $sql = "UPDATE user SET 
        email='{$email}', 
        first_name='{$first_name}',
        last_name='{$last_name}', 
        age='{$age}'
        WHERE id={$id}";
    
        $conn->exec($sql);
    }
```

### Задание 6. - Запрос на удаление

1. После кода, добавляющего кнопку `Изменить`, вставьте код ячейки таблицы со ссылкой на кнопку "Удалить"
```
        // Добавим кнопку Удалить
        $html .= <<<LINE
                     <td>
                        <a href='sql.php?delete&id={$row['id']}'>
                            <input type='button' value='Удалить'>
                        </a>
                     </td>
                    LINE;
```
2. В урл ссылки записан GET-запрос на удаление (параметр delete) с указанным id (параметр id),
добавьте проверку на наличие параметра `delete` в глобальном массиве `$_GET`:
```
    // Обработаем GET с параметром delete - запрос на Удаление
    if (isset($_GET["delete"])) {
        $id = $_GET["id"];
        // Составим запрос
        $sql = "DELETE FROM user WHERE id={$id}";
        $conn->exec($sql);
    }   
```

### Задание 7. - Класс UserDbStorage

1. Создайте класс `UserDbStorage`, конструктор которого создает соединение, сохраняя объект класса PDO в поле `private $connection;`
2. Метод `insert` - добавляет данные из глобального массива `$_POST` SQL запросом в базу данных
3. Метод `update` - отправляет SQL запрос на изменение полученных данные из глобального массива `$_POST`
4. Метод `delete` - удаляет запись с id из глобального массива `$_GET`
5. Метод `list` - получает все записи таблицы, возвращает массив
