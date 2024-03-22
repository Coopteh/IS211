### Задание 1. - Базовый шаблон (улучшение)

Необходимо изменить базовый шаблон, добавив:
- подключение стилей bootstrap
- блок с навигацией
- блок контейнера
  
Откройте файл `templates\BaseTemplate.php` и измените возвращаемое методом `getBaseTemplate()` значение переменной `$template`
- добавьте в секцию head
```
            <link rel="stylesheet" href="./css/bootstrap.min.css">
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
                    $item['name'],
                    $item['name'],
                    $item['name'],
                    $item['name'],
                    $item['price']
                );
```
