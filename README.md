### Задание 1. - Базовый шаблон (улучшение)

Необходимо изменить базовый шаблон, добавив:
- подключение стилей bootstrap
- блок с навигацией
- блок контейнера
  
Откройте файл `templates\BaseTemplate.php` и измените возвращаемое методом `getBaseTemplate()` значение переменной `$template`
- добавьте в секцию head
```
            <link rel="stylesheet" href="https://localhost/css/bootstrap.min.css">
```
- добавьте в секцию body (заменив содержимое в нем)
```
        <div class="container">
            <nav class="navbar navbar-expand-lg bg-body-tertiary mb-2">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">BURGER KRIG</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                    </button>
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                    <a class="nav-link active" aria-current="page" href="#">Главная</a>
                    <a class="nav-link" href="/products.html">Каталог</a>
                    <a class="nav-link" href="/orders/">Сделать заказ</a>
                    </div>
                </div>
                </div>
            </nav>
            %s
        </div>
```
<hr>

### Задание 2. - Шаблон Каталога продукции (улучшение)

Необходимо изменить шаблон вывода списков товаров, добавив в него:
- новые поля, типа картинки, описания, веса
- новую разметку на bootstrap-стилях

Откройте файл `\templates\ProductTemplate.php` и измените в методе `getTemplate`, в теле цикла foreach значение на:
```
            $element_template= <<<END
            <div class="row mb-5">
                <div class="col-6">
                    <img src="%s" class="w-100">
                </div>
                <div class="col-6">
                    <div class="block">
                        <h2>%s</h2>
                        <p>%s</p>
                        <p>%s</p>
                        <h2>%d ₽</h2>
                    </div>
                </div>
            </div>
            END;

            $str.= sprintf(
                    $element_template, 
                    'https://localhost/'.$item['image'],
                    $item['name'],
                    $item['description'],
                    $item['weigth'],
                    $item['price']
                );
```
<hr>

### Задание 3. - Шаблон отдельной страницы товара

Необходимо изменить шаблон отдельной страницы - которая выдается по урл вида `http://localhost/products/1`  
Измените метод `getPageTemplate` класса `ProductTemplate`
```
        $template = parent::getBaseTemplate();

        $element_template= <<<END
        <div class="row mb-5">
            <div class="col-6">
                <img src="%s" class="w-100">
            </div>
            <div class="col-6">
                <div class="block">
                    <h2>%s</h2>
                    <p>%s</p>
                    <p>%s</p>
                    <h2>%d ₽</h2>
                </div>
            </div>
        </div>
        END;

        $str= sprintf(
            $element_template, 
            'https://localhost/'.$arr['image'],
            $arr['name'],
            $arr['description'],
            $arr['weigth'],
            $arr['price']
        );      

        $resultTemplate =  sprintf($template, 'Страница товара', $str);
        return $resultTemplate;
```
<hr>

### Задание 4. - Классы Главной страницы

Необходимо создать класс Главной страницы (Home) на который роутер будет направлять по-умолчанию.
Также понадобятся отдельный шаблон главной страницы (HomeTemplate), ведь на главной у нас есть карусель с картинками и прочая информация.

Класс контроллера `Home`
1. Создайте файл `\controllers\Home.php`
2. Внутри опишите класс `Home` с единственным методом get, который вызывает шаблон и возвращает его в качестве результата
```
    public function get(): string 
    {
        $objTemplate = new HomeTemplate();
        $template = $objTemplate->getHomeTemplate();
        return $template;
    }
```

Класс шаблона главной страницы `HomeTemplate`
1. Создайте файл `\templates\HomeTemplate.php`
2. Внутри опишите класс `class HomeTemplate extends BaseTemplate` с единственным методом getHomeTemplate
```
    public function getHomeTemplate(): string 
    {
        $template = parent::getBaseTemplate();
        $str = <<<END
        <div class="h-50 w-50 mx-auto">
        <div id="carouselExample" class="carousel slide">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="./img/image1.jpg" class="d-block w-100 h-100" alt="1">
            </div>
            <div class="carousel-item">
              <img src="./img/image2.jpeg" class="d-block w-100 h-100" alt="3">
            </div>
            <div class="carousel-item">
              <img src="./img/image3.jpg" class="d-block w-100 h-100" alt="2">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
        </div>
    
    
        <div class="row mt-5">
            <p>
                Приглашаем в наше онлайн-кафе "БУРГЕР КРИГ"!
            </p>
            <p>
                Листайте каталог и добавляйте товар в корзину, нажимая кнопку "Купить".
                Нажмите "Сделать заказ", чтобы окончательно оформить заказ:
            </p>
            <div class="ml-10">
                <ul>
                     <li>узнать итоговую сумму заказа</li>
                    <li>ввести данные для доставки</li>
                    <li>подтвердить заказ</li>
                </ul>
            </div>
        </div>   
        <script src="./js/bootstrap.bundle.min.js" type="text/javascript"></script>
        END;
        $resultTemplate =  sprintf($template, 'Главная страница', $str);
        return $resultTemplate;
    }
```

Изменения в роутере - главная страница - маршрут по-умолчанию.
Откройте класс `Router`, метод `route(string $url):string`, внутри свича (switch-case) измените опцию `default:`
```
            default:
                $home = new Home();
                $html_result = $home->get();
                break;
```
- вызываем контроллер и его метод `get` для получения заполненного шаблона

Дополнительно:
```
в Basetemplate - измените ссылки в блоке nav на
                    <a class="nav-link active" aria-current="page" href="/">Главная</a>
                    <a class="nav-link" href="/products">Каталог</a>
                    <a class="nav-link" href="/orders">Сделать заказ</a>

Во всех скриптах поменяйте include на include_once
```
Теперь можно сократить `index.php` до:
```
<?php 
	 include("./routers/Router.php");
	
	 $router = new Router();
	 $url = $_SERVER['REQUEST_URI'];

	 echo $router->route($url);
```
<hr>

### Задание 5. - Добавление товара в корзину

На странице Каталог - добавьте кнопки `Купить` (код кнопок писали ранее в `add_cart.html`)
