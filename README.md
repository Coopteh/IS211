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
<hr>

### Задание 2 - Добавление карусели изображений

1. На сайте Bootstrap  [https://getbootstrap.com/](https://getbootstrap.com/) зайдите в раздел `Docs \ Components \ Carousel \ Basic examples`
2. Скопируйте код карусели и вставьте над формой
3. Найдите 3 картинки бургеров и сохраните их в папку `img` (создайте папку внутри c:\xamp\htdocs\)
4. Исправьте в html-коде карусели атрибуты `src` тегов `img`, чтобы они указывали на нужные картинки (пример <img src="./img/image1.png">)
5. Проверьте работу карусели изображений на сайте `localhost`
<hr>

### Задание 3 - Добавление навигационной панели

1. На сайте Bootstrap  [https://getbootstrap.com/](https://getbootstrap.com/) зайдите в раздел `Docs \ Components \ Navbar`
2. Скопируйте код навигационной панели без кнопок и форм
```
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <a class="nav-link active" aria-current="page" href="#">Home</a>
        <a class="nav-link" href="#">Features</a>
        <a class="nav-link" href="#">Pricing</a>
        <a class="nav-link disabled" aria-disabled="true">Disabled</a>
      </div>
    </div>
  </div>
</nav>
```
6. Создайте меню с пунктами "Главная", "Каталог", "Сделать заказ"
7. Измените ссылки "Каталог" на "/products/", а "Сделать заказ" на "/orders/"
