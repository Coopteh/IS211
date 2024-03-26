### Задание 1. - Класс корзины Basket

1. Создайте класс `Basket` в папке `controllers` и добавьте 2 метода `add` и `clear`
2. Добавьте код из файла `add.php` в метод `add` класса `Basket`
```
удалите все echo
добавьте возвращаемое значение
return "Товар успешно добавлен в корзину!";
```
4. Добавьте код из файла `clear.php` в метод `clear` класса `Basket`
```
добавьте возвращаемое значение
return "";
```
6. В коде разметки `ProductTemplate` измените `action` для форм на `action="/basket"`, а метод на `method="POST"`
7. В коде разметки `Order` измените `action` для форм на `action="/basket_add"`, а метод на `method="POST"`
8. Добавьте в класс маршрутизации `Router` определение http-метода (перед switch)
```
      // метод GET, POST, DELETE
    	$method = $_SERVER['REQUEST_METHOD'];
```
7. Добавьте в класс маршрутизации `Router` обработку урл `/basket` и `/basket_add` для метода `POST`
```
/basket, POST - ведет к созданию класса Basket и вызову его метода add()
/basket_add, POST - ведет к созданию класса Basket и вызову его метода clear()

            case "basket":
                $basket = new Basket();
                if ($method == "POST")
                    $html_result = $basket->add();
                break;   
            case "basket_add":
                $basket = new Basket();
                if ($method == "POST")
                    $html_result = $basket->clear();
                break;   
```
<hr>

### Задание 2. - Добавление сообщения "Товар добавлен"

После нажатия на кнопку "Добавить в корзину" необходимо сделать всплывающее окно  
с сообщением об успешном добавлении товара в корзину.

1. В методе `add` класса `Basket` добавьте в конце добавление новой сессионной переменной $_SESSION['flash']
и переадресацию обратно - на страницу Каталога 
```
            $_SESSION['flash'] = "Товар успешно добавлен в корзину!";
            header('Location: /products');
            return "";
```
3. В методе `getTemplate` класса `ProductTemplate` добавьте после `$str= '';`
```
        // Добавим flash сообщение
        session_start();
        if (isset($_SESSION['flash'])) {
            $str .= <<<END
                <div class="alert alert-success" role="alert">
                    {$_SESSION['flash']}
                </div>
            END;
            unset($_SESSION['flash']);
        }
```
