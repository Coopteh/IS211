# Паттерн "Заместитель" (Proxy)
используется для управления доступом к другому объекту, другое название - Суррогат  
структурный паттерн  

**Назначение:**  
одна и причин для управления доступом к объекту - возможность отложить  
затраты на создание и инициализацию объекта до момента, когда в нем возникнет фактическая необходимость.

Рассмотрим пример
```
from typing import Dict

# Общий интерфейс
class ISite:
    def get_page(self, num: int) -> str:
        pass


# Реальный сайт
class Site(ISite):
    def get_page(self, num: int) -> str:
        return "Это страница {}".format(num)


# Заместитель (Proxy)
class SiteProxy(ISite):
    def __init__(self, site: ISite):
        self.__site = site
        self.__cache: Dict[int, str] = {}

    def get_page(self, num: int) -> str:
        page: str = ''
        if self.__cache.get(num) is not None:
            page = self.__cache[num]
            page = "из кеша: " + page
        else:
            page = self.__site.get_page(num)
            self.__cache[num] = page
        return page
```
Использование:
```
def main():
    my_site: ISite = SiteProxy(Site())

    print(my_site.get_page(1))
    print(my_site.get_page(2))
    print(my_site.get_page(3))

    print(my_site.get_page(1))
    print(my_site.get_page(2))


if __name__ == "__main__":
    main()
```
В этом примере:
- ISite - интерфейс, определяющий общие операции для реального сервиса и заместителя.  
- Site - реальный объект, предоставляющий специфическую функциональность.  
- SiteProxy - заместитель, обеспечивающий доступ к реальному объекту, контролируя его создание и жизненный цикл.  
 
Паттерн "Заместитель" позволяет установить контроль над доступом к другому объекту,  
прозрачно добавляя функциональность до, после и вместо выполнения запросов к реальному объекту.  

### Задание
- создайте задержку времени выполнения для класса Site - в методе get_page  
запишите задержку на выполнение в 10 секунд  
используйте  
```
import time
time.sleep(10)  # Задержка на 10 секунд
```
