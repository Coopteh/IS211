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
      $class = str_replace('\\', DIRECTORY_SEPARATOR, $className);
      $path = __DIR__ . "/{$class}.php";
      if (is_readable($path))
          require_once $path;
}

spl_autoload_register("autoloadClasses");
```
3. Подключите файл `autoload.php` в `index.php` через `require_once(./autoload.php)`
4. Проверьте будет ли работать сайт (он должен работать без изменений)

### Задание 3. - Менеджер загрузки Composer

1. Установите менеджер загрузки готовых компонентов Composer в свой проект
```
Наберите в папке проекта, в адресной строке:
cmd
Затем вызовите инициализацию:
composer init
```
Подключите автозагрузчик composer к проекту. Для этого в файл autoload.php (в корне проекта) добавьте подключение файла vendor/autoload.php — это позволит автоматически загружать классы зависимостей composer.

### Задание 4. - Отправка емайл

https://debugmail.io/

В командной строке ОС перейдите в корневую папку проекта и с помощью команды `composer require phpmailer/phpmailer` установите библиотеку PHPMailer. 
После сохранения заказа, и если пользователь ввёл email, отправьте копию текста на его email. 
Для этого используйте PHPMailer. 
Обязательно оборачивайте вызовы методов PHPMailer в try .. catch. 
Если возникла какая-либо ошибка при отправке сообщения — выведите соответствующее флеш-предупреждение в красном блоке (error).

