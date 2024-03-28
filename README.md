### Задание 1. - Пространство имен

1. Необходимо добавить в каждый файл с исходным кодом пространство имен, типа:  
`namespace Controllers\Home;`
2. Добавьте использование других пространств имен, а именно
вместо `include_once("./templates/HomeTemplate.php");`
используйте импортирование пространства имен `use Templates\HomeTemplate;`
3. Избавьтесь от всех `require_once, include_once` - подключение классов будем делать через автозагрузчик
4. Создайте автозагрузчик классов - в корне сайта файл `autoload.php`
5. Используйте функцию автозагрузки [spl-autoload-register](https://www.php.net/manual/en/function.spl-autoload-register.php)  
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
6. Подключите файл `autoload.php` в `index.php` через `require_once(./autoload.php)`
7. Проверьте будет ли работать сайт
