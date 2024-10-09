### Задание 1. - Создание модульных тестов для проекта BurgerKrig

Необходимо:  
- добавить в проект инструмент автоматизированного тестирования PHPUnit  
- создать модульные тесты для phpUnit, повторить навык их написания и запуска  

**1. Воскресим проект BurgerKrig на виртуальном хостинге**

Запустите виртуальный сервер XAMPP (кнопка Apache), в папке `/c/xampp/htdocs` удалите все файлы  
Работайте в GitBash - перейдите в папку `/c/xampp/htdocs` и клонируйте репозиторий `https://github.com/Coopteh/BurgerKrig`  
Переключитесь на ветку `final_with_json`  
Переместите все файлы (в Проводнике) так чтобы файл `index.php` был в корне папки `/c/xampp/htdocs` (остальные файлы и папки тоже согласно своим местам)  
Выполните все зависимости проекта, запустив менеджер зависимостей `composer install`  
Проверьте запустился ли сайт по `localhost`  
Создайте (в корне сайта) файл `.gitignore` в который добавьте папку `vendor/`  
Теперь добавьте файлы в репозиторий командой `git add *`, зафиксируйте изменения `git commit -m "Добавлен файл .gitignore"`  
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

```
Выполните тесты командой `vendor/bin/phpunit tests`
Если тест выполняется успешно - зафиксируйте изменения и передайте на сервер командой `git push` (она ругнется, но предложит работающий вариант с --set-upstream, выполните его)  
Убедитесь что на `https://github.com/Coopteh/BurgerKrig` появилась ваша новая ветка  

