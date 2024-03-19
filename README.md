### Задание 1 - Подключение Bootstrap

Bootstrap — свободный набор инструментов для создания сайтов и веб-приложений.  
Включает в себя HTML- и CSS-шаблоны оформления для типографики, веб-форм, кнопок, меток,  
блоков навигации и прочих компонентов веб-интерфейса, включая JavaScript-расширения.

Задание - подключить стили и js-библиотеку Bootstap   
и добавить пример формы из документации, чтобы проверить работу шаблона

Шаги выполнения:
1. Откройте в Visual Studio Code папку `c:\xamp\htdocs\index.php`
2. Откройте в браузере ссылку [https://getbootstrap.com/](https://getbootstrap.com/)
3. Найдите в меню `Docs \ Download \ Source files \ Download sources` - скачайте архив
4. Найдите в нем папку `dist` и скопируйте файлы:
```
bootstrap.bundle.min.js  -  в новую папку js (создайте папку внутри c:\xamp\htdocs\)
bootstrap.min.css  -  в новую папку css (создайте папку внутри c:\xamp\htdocs\)
```
5. Подключите таблицу стилей `bootstrap.min.css` в конце секции `head` (тег `<link rel="stylesheet" href="...">`)
6. Подключите js-скрипты `bootstrap.bundle.min.js` в конце секции `body` (тег `<script src="..."></script>`)
7. Добавьте блок
```
<div class="container">
	<div class="row">

	</div>
</div>
```
8. Внутрь блока добавьте html-код формы из документации (`Docs \ Forms \ Form controls \ Example`)
9. Подключите плагин эмитов `Bootstrap 5` (вызываются через `b5<Tab>`)  
10. Запустите `Xampp Control` в нем запустите `Apache`
11. Откройте в браузере `localhost` - форма должна отображаться в стилях Bootstrap!

