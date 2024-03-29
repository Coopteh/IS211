### Задание 1. - Пространство имен

1. Переименуйте все каталоги, содержащие исходный код в названия с первой заглавной буквой  
```
Controllers, Services, Templates, Interfaces, Routers
```
2. Необходимо добавить в каждый файл с исходным кодом пространство имен, типа:  
`namespace Controllers;`
Именование namespace-ов следует давать по названиям каталога (иначе будет ошибка), то есть
```
namespace Controllers;      // для каталога Controllers
namespace Routers;          // для каталога Routers
```

3. Добавьте использование других пространств имен, а именно:
вместо `include_once("./templates/HomeTemplate.php");`
используйте импортирование пространства имен `use Templates\HomeTemplate;`
```
use Templates\HomeTemplate;      // это соответствует файловой структуре - в директории Templates лежит файл HomeTemplate.php c нужным нам классом HomeTemplate
```
5. Избавьтесь от всех `require_once, include_once` - подключение классов будем делать через автозагрузчик
<hr>

### Задание 2. - Автозагрузчик классов  

1. Создайте автозагрузчик классов в корне сайта - файл `autoload.php`
2. Используйте функцию автозагрузки [spl-autoload-register](https://www.php.net/manual/en/function.spl-autoload-register.php)  
Функция регистрирует пользовательскую функцию в очереди __autoload SPL-библиотеки ядра PHP.
Напишите в файл `autoload.php` следующее содержимое:
```
<?php
function autoloadClasses($className)
{
    $class = str_replace('\\', '/', $className);
    $path = "./". $class.".php";
    if (file_exists($path)) {
        require_once($path);
    }
}

spl_autoload_register("autoloadClasses");
```
3. Подключите файл `autoload.php` в `index.php` через `require_once("./autoload.php");`
4. Проверьте будет ли работать сайт (он должен работать без изменений)

### Задание 3. - Менеджер загрузки Composer

1. Установите менеджер загрузки готовых компонентов Composer в свой проект
```
Наберите в папке проекта, в адресной строке:
cmd
Затем вызовите инициализацию:
composer init
```
Подключите автозагрузчик composer к проекту.  
Для этого в файл index.php (в корне проекта) добавьте подключение файла `vendor/autoload.php` (вместо `require_once("./autoload.php");`)
```
require_once("./vendor/autoload.php");
```
— это позволит автоматически загружать классы зависимостей composer
Измените файл настроек менеджера зависимостей `composer.json`
```
{
    "name": "burger/krig",
    "autoload": {
        "psr-4": {
            "": ""
        }
    },
    "authors": [
        {
            "name": "Coop Teh",
            "email": "v.milevskiy@coopteh.ru"
        }
    ],
    "require": {}
}
```
Запустите `composer install` чтобы изменения вступили в силу.  
Проверьте работает ли проект.

### Задание 4. - Отдельная папка для исходного кода проекта 

Лучшим решением будет собрать весь исходный код проекта в отдельную папку `BurgerKrig`  
1. Создайте папку `BurgerKrig` внутри папки `c:\xampp\htdocs` скопируйте в нее все директории с кодом:
Controller, Templates, Routers, Interfaces, Services, css, img, js
2. Отредактируйте `composer.json` изменив 5-ю строчку на `"": "BurgerKrig/"`
```
{
    "name": "burger/krig",
    "autoload": {
        "psr-4": {
            "": "BurgerKrig/"
        }
    },
```
3. Запустите `composer install` чтобы изменения вступили в силу.  
Теперь все классы будут искаться в этой папке.  
Проверьте работает ли проект.

### Задание 5. - Отправка емайл

Главная задача - научиться расширять проект за счет использования сторонних компонентов   
с помощью их добавления через менеджер компонентов Composer  
на примере майлера для отправки писем PhpMailer  

1. Зайдите на страницу компонета майлера [PHPMailer](https://github.com/PHPMailer/PHPMailer)  
найдите в рубрике "Installation & loading" строку установки через Composer (типа - composer requare ..)
выполните установку компонента
```
composer require phpmailer/phpmailer
```
Вы установили компонент PHPMailer, проверьте он должен появиться в папку `vendor`

2. Откройте временный ящик, например на `https://temp-mail.org/`
для получения почты на этот временный email
3. В классе `Order` создайте новый метод
4.
5. После сохранения заказа, и если пользователь ввёл email, отправьте копию текста на его email.   
Для этого используйте PHPMailer. 
Обязательно оборачивайте вызовы методов PHPMailer в try .. catch. 
Если возникла какая-либо ошибка при отправке сообщения — выведите соответствующее флеш-предупреждение в красном блоке (error).
```
    $mail = new PHPMailer();
    if (isset($_POST['email']) && !empty($_POST['email'])) {
        try {
            $mail->CharSet = 'UTF-8';
            $mail->setFrom('');
            $mail->addAddress('u');
            $mail->isHTML(true);
            $mail->isSMTP();                                            //Send using SMTP
            $mail->Host       = 'smtp.yandex.ru';                     //Set the SMTP server to send through
            $mail->SMTPAuth   = true;                                   //Enable SMTP authentication
            $mail->Username   = '';                     //SMTP username
            $mail->Password   = '';
            $mail->Subject = 'Заявка с сайта: Telegraph.com';
            $mail->Port       = 465;
            $mail->SMTPSecure = 'ssl';            //Enable implicit TLS encryption
            $mail->Body = 'Информационное сообщение c сайта Telegraph.com <br><br>
            ------------------------------------------<br>
            <br>
            Вам было отправлено сообщение через форму обратной связи<br>
            <br>
            Текст: ' . $_POST['text'] . '<br>
            <br>
            Сообщение сгенерировано автоматически.';

            if ($mail->send()) {
                $myError = '<div class="mail success">
                Ваше письмо успешно отправленно!
                 </div>';
            } else {
                throw new Exception('<div class="mail error">Что-то пошло не так!<br><br>Повторите попытку.</div>');
            }
        } catch (Exception $error) {
            $myError =  $error->getMessage();
        }
    }
```
