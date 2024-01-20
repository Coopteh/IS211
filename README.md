# TODO
## A. Создайте удаленный репозиторий
1. Перейдите в папку с проектами вашей группы
```
cd PycharmProjects/IS211
```
2. Создайте новую папку
```
mkdir task-200124
```
3. Перейдите в новую папку проекта
```
cd task-200124
```
4. Создайте локальный репозиторий
```
git init
```
5. Закрепите удаленный репозиторий к локальному под именем origin
```
git remote add origin https://github.com/Coopteh/IS211.git
```
## B. Написание кода
1. Открыть в pyCharm папку ~/PycharmPython/IS211/oop1
2. Создать новый файл oop1.py
3. Создать новый класс Animal
```
class Animal:
     def __init__(self, name, count)
         self.name = name
         self.count = count

     def __show_details(self):
         print(f"Животное {self.name} имеет {self.count} ноги")
```
5. Создать экземпляр класса Animal и вызвать метод show_details()
```
obj = Animal('корова', 4)
obj.__show_details()
```
6. Если программа успешно работает - передайте код на удаленные репозиторий
   - добавьте файл (в Git Bash) в репозиторий
     git add .
   - закоммитьте изменения
     git commit -m "Added new file"
   - git push --set-upstream origin <название_вашей_ветки>
  
## С. Инкапсуляция, наследование и полиморфизм
1. Создайте 3 класса - дочерний от Animal (от родительского) Dog, Cat, Cow
```
class Dog(Animal):
     pass
class Cat(Animal):
     pass
class Cow(Animal):
     pass
```
2. В самом классе Animal инкапсулируйте поля name и count
```
class Animal:
     def __init__(self, name, count)
         self.__name = name
         self.__count = count

     def show_details(self):
         print(f"Животное {self.__name} имеет {self.__count} ноги")
```
3. Попробуйте обратиться к полям Animal
```
print(obj.__name)
мы получим ошибку - потому что поле скрыто для внешнего мира (инкапсулировано)
напишем метод доступа к приватному свойству self.__name для класса
     def get_name(self):
          return self.__name
теперь мы можем обратиться к свойству через метод его чтения (геттер)
print(obj.get_name())
```
4. Создайте новые объекты классов Dog, Cat, Cow
```
obj_dog = Dog(...)
obj_cat = Cat(...)
obj_cow = Cow(...)
```
5. Добавьте их в список и в цикле вызовите метод show_details для всех созданных объектов
```
obj_list = [obj_dog, ... ]
for obj in obj_list:
     obj.show_details()
```

   
