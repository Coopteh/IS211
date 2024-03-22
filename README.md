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

