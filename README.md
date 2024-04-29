### Задание 1. - Тестирование API через Postman

Скачайте программу установки `Postman` по [ссылке](https://www.postman.com/downloads/?utm_source=postman-home)  
Установите программу - логин: `v.milevskiy@coopteh.ru` (либо сами зарегайтесь)  

1. Создайте `Test-211-Collection`
2. Создайте новый запрос `Add request` с именем 'get-products' для урл `localhost\products`
3. Запустите `Xampp Control Panel \ Apache` и запустите запрос на выполнение в `Postman`
4. Найдите статус `200` и результаты ответа (`Responce`)
5. Создайте новый запрос `Add request` с именем 'get-product-1' для урл `localhost\products\1` и запустите на выполнение
<hr>

### Задание 2. - тестирование POST-запроса

1. Создайте в `Postman` новую коллекцию `Reqres-Collection`
2. Зайдите на ресурс [https://reqres.in/](https://reqres.in/) и скопируйте `Register - successful`
3. Создайте POST-запрос с указанным url (параметры `raw`, `JSON`) и выполните его в `Postman`, сохраните запрос как `Registration`
4. Создайте GET-запрос с url из запроса `List users` (на указанном сайте) и выполните его в `Postman`, сохраните запрос как `List users`
5. Выполните все тесты одной коллекции.
6. Добавьте переменную (Variables) `url` для коллекции
7. Создайте GET-запрос с url из запроса `Single user` используя переменную `url` (для вставки используйте `{{}}`) и выполните его в `Postman`, сохраните запрос как `Single user`
