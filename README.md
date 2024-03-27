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
7. В коде разметки `Order` измените `action` для форм на `action="/basket_clear"`, а метод на `method="POST"`
8. Добавьте в класс маршрутизации `Router` определение http-метода (перед switch)
```
      // метод GET, POST, DELETE
    	$method = $_SERVER['REQUEST_METHOD'];
```
7. Добавьте в класс маршрутизации `Router` обработку урл `/basket` и `/basket_add` для метода `POST`
```
/basket, POST - ведет к созданию класса Basket и вызову его метода add()
/basket_clear, POST - ведет к созданию класса Basket и вызову его метода clear()

            case "basket":
                $basket = new Basket();
                if ($method == "POST")
                    $html_result = $basket->add();
                break;   
            case "basket_clear":
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
                <div id="liveAlertBtn" class="alert alert-success alert-dismissible" role="alert">
                    <div>{$_SESSION['flash']}</div>
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"
                    onclick="this.parentNode.style.display='none';"></button>
                </div>
            END;
            unset($_SESSION['flash']);
        }
```
для автоматического исчезновения (через 3 сек) добавьте, после добавления разметки блока с флеш-сообщением,  
следующий скрипт (опционально, по-желанию):
```
    <script>
            setTimeout(
                function() {
                  var elem = document.getElementById("liveAlertBtn");
                  elem.style.display = "none";
                }, 3000
              );
    </script>
```
<hr>

### Задание 3. - Добавление строки "Общая сумма заказа"

Добавьте суммирование для заказа (Order) всех товаров в Корзине  
и вывод строки "Общая сумма заказа" в разметку "Создание заказа".  
<hr>

### Задание 4. - Добавление формы доставки 

На страницу заказа необходимо добавить разметку с формой заказа - `action="/orders"` `method="POST"`  
В конце метода `get` класса `Order` добавьте (перед `$objTemplate = new OrderTemplate();`)
```
        // Форма ввода данных для доставки заказа
        $str_list .= <<<LINE
        <div class="row">
            <div class="col-12">
                  ...
            </div>
        </div>
        LINE;
```
Внутри формы определите поля:
- ФИО покупателя (input) c label "Ваше ФИО:"
- Адрес покупателя (input) c label "Адрес доставки:"
- Телефон покупателя (input) c label "Телефон:"
- Кнопка (`submit`) "Создать заказ"

Подсказка* - элементы формы лучше взять с сайта bootstrap [https://getbootstrap.com/](https://getbootstrap.com/)   
маршрут `Docs \ Forms \ Form controls`

Настройте роутер на получение данных и вызов метода `create` объекта `Order`

### Задание 5. - Запись заказа в файл

Измените метод `create` класса `Order`, чтобы переданные данные в массиве `$_POST` + время создания заказа (`created_at`)  
записывались в файл `orders.json` - используйте `FileStorage` и его метод `saveData`  
Также добавьте список продуктов к заказу из массива сессии (`$_SESSION`)  
Итого (для передаваемых полей `fio, address, phone`):
```
        $objStorage = new FileStorage();

        $arr = [];
        $arr['fio'] = urldecode( $_POST['fio'] );
        $arr['address'] = urldecode( $_POST['address'] );
        $arr['phone'] = $_POST['phone'];
        $arr['created_at'] = date("d-m-Y H:i:s");

        $products = $objStorage->loadData('data.json');
        session_start();
        $all_sum = 0;
        $items = [];
        foreach ($products as $product) {
            $id = $product['id'];
            if (array_key_exists($id, $_SESSION['basket'])) {
                $item = [];
                $item['name'] = urldecode( $product['name'] );
                $item['quantity'] = $_SESSION['basket'][$id]['quantity'];                
                $item['price'] = $product['price'];
                $item['sum'] = $item['price'] * $item['quantity'];
                $all_sum += $item['sum'];
                array_push($items, $item);
            }
        }
        $arr['all_sum'] = $all_sum;
        $arr['products'] = $items;

        $objStorage->saveData('orders.json', $arr);
        return 'Вызван метод create() из класса Order';
```
также следует изменить метод `saveData` класса  `FileStorage`  
```
        if (filesize($nameFile) > 0) {
            $data = $this->loadData($nameFile);
        } else
            $data = [];
        array_push($data, $arr);

        $json = json_encode($data, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
        
        $handle = fopen($nameFile, "w");
        fwrite($handle, $json);
        fclose($handle);
```
Добавление заказов можно проверить в файле `orders.json`

Для самостоятельной работы:
- после успешной записи заказа в файл - очистите корзину
- выдайте флеш-сообщение "Спасибо! Ваш заказ успешно создан и передан службе доставки"
с переадресацией на главную страницу  
