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
         self.__name = name
         self.__count = count

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
   
