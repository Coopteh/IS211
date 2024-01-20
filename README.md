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

## B.
1. Открыть в pyCharm папку ~/PycharmPython/IS211/oop1
2. Создать новый файл oop1.py
3. Создать новый класс Animal
```
class Animal:
     def __init__(self, name, count)
         self.name = name
         self.count = count

     def show_details(self):
         print(f"Животное {self.name} имеет {self.count} ноги")
```
5. Создать экземпляр класса Animal и вызвать метод show_details()
```
obj = Animal('корова', 4)
obj.show_details()
```
6. Если программа успешно работает - передайте код на удаленные репозиторий
   - добавьте файл (в Git Bash) в репозиторий
     git add .
   - закоммитьте изменения
     git commit -m "Added new file"
   - git push --set-upstream origin
   
