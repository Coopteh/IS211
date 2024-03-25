### Задание 1. - Класс корзины Basket

1. Создайте класс `Basket` в папке `controllers` и добавьте 2 метода `add` и `clear`
2. Добавьте код из файла `add.php` в метод `add` класса `Basket`
3. Добавьте код из файла `clear.php` в метод `clear` класса `Basket`
4. В коде разметки `ProductTemplate` измените `action` для форм на `action="/basket"`, а метод на `method="POST"`
5. В коде разметки `Order` измените `action` для форм на `action="/basket"`, а метод на `method="DELETE"`
6. Добавьте в класс маршрутизации `Router` обработку урл `/basket` и двух методов `POST` и `DELETE`
```
/basket, POST - ведет к созданию класса Basket и вызову его метода add()
/basket, DELETE - ведет к созданию класса Basket и вызову его метода clear()
```
