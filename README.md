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
2. Откройте временный ящик, например на [https://temp-mail.org/](https://temp-mail.org/)  
для получения почты на этот временный email  
3. В классе `Order` укажите импортирование пространств имен используемых классов PHPMailer  
```
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
```  
4. В классе `Order` создайте новый метод `sendMail($email)`  
```
    public function sendMail($email) {
        $mail = new PHPMailer();
        if (isset($email) && !empty($email)) {
            try {
                $mail->SMTPDebug = 2;
                $mail->CharSet = 'UTF-8';
                $mail->SetFrom("v.milevskiy@coopteh.ru","Burger krig");
                $mail->addAddress($email);
                $mail->isHTML(true);
                $mail->isSMTP();                                            //Send using SMTP
                $mail->Host       = 'ssl://smtp.mail.ru';                     //Set the SMTP server to send through
                $mail->SMTPAuth   = true;                                   //Enable SMTP authentication
                $mail->Username   = 'v.milevskiy@coopteh.ru';                     //SMTP username
                $mail->Password   = 'hF8xTWxXyKcCnEg1n9Wz';
                $mail->Port       = 465;
                $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;            //Enable implicit TLS encryption
                $mail->Subject = 'Заявка с сайта: Burger Krig';
                $mail->Body = 'Информационное сообщение c сайта Burger Krig <br><br>
                ------------------------------------------<br>
                <br>
                Спасибо!<br>
                <br>
                Ваш заказ успешно создан и передан службе доставки.<br>
                <br>
                Сообщение сгенерировано автоматически.';       
    
                if ($mail->send()) {
                    return true;
                } else {
                    throw new Exception('Ошибка с отправкой письма');
                }
            } catch (Exception $error) {
                $message =  $error->getMessage();
            }
        }    
        return false;
    }
```
Майлер настроен на отправку писем через почтовый сервер `smtp.mail.ru` с логином `v.milevskiy@coopteh.ru` и соответствующим паролем.    
Письмо составляется в формате HTML методом `send()`    
Ошибки ловятся в в try .. catch через генерацию исключения `throw new Exception('Ошибка с отправкой письма');` в случае неудачной отправки  
обработки ошибок нет, оставлено для самостоятельной работы (можно, например, записывать в лог-файл)

5. Добавьте email в форму заказа (класс `Order`, метод `get`)
```
<label for="email">Email:</label>
<input type="email" id="email" class="form-control" name="email" required>
```
сразу после поля ввода телефона  
7. Добавьте вызов метода отправки емайл (класс `Order`, метод `create`) сразу после сохранения данных   
```
$objStorage->saveData('orders.json', $arr);
// отправка емайл
$this->sendMail($_POST['email']);
```
8. Проверьте отправку емайл:
```
Создайте заказ, указав в качестве емайла пользователя - временный емайл с temp-mail.org
После выдачи сообщения "Спасибо! Ваш заказ успешно создан и передан службе доставки" - проверьте temp-mail.org
Откройте письмо во входящих для проверки содержимого.
```
