### Задание 1. - Класс заказа Order

1. Откройте класс `Order` в папке `controllers` и добавьте метод `get`, который вызывает шаблон из класса `OrderTemplate`
```
    public function get(): string
    {
        session_start();

        $objStorage = new FileStorage();
        $products = $objStorage->loadData('data.json');

        $all_sum = 0;
        $str_list = '';
        foreach ($products as $product) {
            $id = $product['id'];
            if (array_key_exists($id, $_SESSION['basket'])) {
                $quantity = $_SESSION['basket'][$id]['quantity'];
                $name = $product['name'];
                $price = $product['price'];

                $sum = $price * $quantity;
                $all_sum += $sum;
                $str_list .= <<<LINE
                <div class="row">
                    <div class="col-6">
                    {$name}
                    </div>
                    <div class="col-2">
                    {$quantity}
                    </div>
                    <div class="col-2">
                    {$sum}
                    </div>
                </div>
                LINE;
            }
        }

        $objTemplate = new OrderTemplate();
        $template = $objTemplate->getTemplate( $str_list );

        return $template;
    }
```
3. Создайте класс `OrderTemplate` в папке `templates`
4. Создайте метод `getTemplate(string $str_list): string`
```
        $template = parent::getBaseTemplate();
        $resultTemplate = sprintf($template, 'Создать заказ', $str_list);
        return $resultTemplate;
```
5. Зайдите в Каталог и добавьте пару товаров в корзину, нажмите "Создать заказ" - вы должны увидеть список товаров и подсчитанную сумму заказа.
