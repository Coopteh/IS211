### Задание 1. - Создание модульных тестов для проекта BurgerKrig

Необходимо:  
- добавить в проект инструмент автоматизированного тестирования PHPUnit  
- создать модульные тесты для phpUnit, повторить навык их написания и запуска  

**1. Воскресим проект BurgerKrig на виртуальном хостинге**

Запустите виртуальный сервер XAMPP (кнопка Apache), в папке `/c/xampp/htdocs` удалите все файлы  
Работайте в GitBash - перейдите в папку `/c/xampp/htdocs` и клонируйте репозиторий `https://github.com/Coopteh/BurgerKrig`  
Перейдите в папку `BurgerKrig` и переключитесь на ветку `final_with_json`  
Переместите все файлы и папки (в Проводнике, поставив галочку "Скрытые файлы") из каталога `BurgerKrig` в `c/xampp/htdocs`,  
так чтобы файл `index.php` был в корне папки `/c/xampp/htdocs`   
Выполните все зависимости проекта, запустив менеджер зависимостей `composer install`  
Проверьте запустился ли сайт по `localhost` (в браузере)   
Создайте (в корне сайта) файл `.gitignore` в который строку `vendor/` (добавит папку как игнорируемый путь для git)  
Теперь добавьте новые и измененные файлы в локальный репозиторий командой `git add *`,   
зафиксируйте изменения `git commit -m "Добавлен файл .gitignore"`  
Сайт запускается и работает!  
<hr>

**2. Добавим PHPUnit в проект**

Создайте новую ветку `auto-test-N`, где N - номер вашего компа и перейдите на нее  
В консоле запустите  `composer require --dev phpunit/phpunit` (установка компонента запуска модульных тестов phpunit для dev- окружения)  
Проверьте что компонент установлен, вызвав `vendor/bin/phpunit --version`
Создайте в корне сайта папку  `tests`  
Отредактируйте `composer.json` - добавив секцию `autoload-dev`  
```
    "autoload-dev": {
        "psr-4": {
            "Test\\": "tests/"
        }
    },
```
эта секция указывает в какой папке находится пространство имен "Test"  
Чтобы изменения вступили в силу - запустите вновь менеджер зависимостей `composer install`  
Теперь добавьте файлы в репозиторий командой `git add *`, зафиксируйте изменения `git commit -m "Добавлен phpUnit"`  
<hr>

**3. Создаем и запускаем модульные тесты для проекта**

Создадим модульные тесты для проверки работы роутера - его метод `route($url): string`   
- получает URL страницы сайта и выдает строку в виде подготовленной веб-страницы с html-кодом
В папке `tests` создайте файл `RouterTest.php` с классом `RouterTest` следующего содержания:
```
<?php 
namespace Test;

use PHPUnit\Framework\TestCase;
use Routers\Router;

class RouterTest extends TestCase {
    public function test_router() {
        $router = new Router();
        $html = $router->route( "http://localhost/orders" );
        $pos= mb_strpos($html, "Создание заказа");
        $this->assertNotEquals(false, $pos);
    }
}
```
тест `test_router()` проверяет есть ли на странице, выдаваемой методом `route()` для урл `http://localhost/orders`, текст `Создание заказа`  
Выполните тесты командой `vendor/bin/phpunit tests`  
Если тест выполняется успешно - зафиксируйте изменения и передайте на сервер командой `git push`  
(она ругнется, но предложит работающий вариант с --set-upstream, выполните его)  
Убедитесь что на `https://github.com/Coopteh/BurgerKrig` появилась ваша новая ветка  
<hr>

**4. Самостоятельная работа**

Добавьте еще пару проверок теста `RouterTest`:  
- проверка главной страницы:
```
есть ли на странице, выдаваемой методом route() для урл "http://localhost", текст "Приглашаем в наше онлайн-кафе"  
```
- проверка страницы "Каталог":
```
есть ли на странице, выдаваемой методом route() для урл "http://localhost/products)", текст "Добавить в корзину"
```
<hr>

**5. Создание пайплайна**

В корне сайта создайте папку `.github`, перейдите в нее и создайте еще подпапку `workflows` (должно получиться `.github/workflows`)  
Перейдите в `.github/workflows` и создайте файл `deploy.yml`, добавив в него следующее содержание  
```
name: PHP_CI_BURGERKRIG

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Setup PHP
        uses: shivammathur/setup-php@v2
        with:
          php-version: '8.2'

      - name: Install dependencies
        run: composer install

      - name: Run PHPUnit tests
        run: ./vendor/bin/phpunit tests
```
В секции `on` измените ветку с `main` на свою `auto-test-N`, где N - номер вашего компа  
(чтобы триггерить выполнение пайплайна на событие пуша в свою ветку)  
Вы создали пайплайн для CI на GitHub Actions, поздравляем!  

Зафиксируйте изменения и передайте на сервер командой `git push`   
зайдите на страницу `Action` репозитория `https://github.com/Coopteh/BurgerKrig` и убедитесь, что пайплайн успешно выполнился и тесты пройдены.  
