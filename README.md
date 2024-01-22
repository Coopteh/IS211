# TODO

## A. Создайте локальный репозиторий
Вызовите Git Bash
Перейдите в папку с проектами пайтона
```
cd PycharmProjects
```
1. Перейдите в папку с проектами вашей группы IS211
`cd IS211`   
либо создайте ее (папку IS211) командой `mkdir IS211`  
2. Создайте новую папку
```
mkdir task-220124
```
3. Перейдите в новую папку проекта
```
cd task-220124
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
1. Открыть в pyCharm папку ~/PycharmProjects/IS211/task-220124
2. Создать новый файл animal.py
3. Создать новый класс Animal
Создайте класс Animal с инициализатором принимающим параметр name (имя животного)
и методом speak, который выводит (print(f"...")) поля имя животного и звук который оно издает ("неизвестный звук" для класса Animal)
4. Создайте еще 3 класса Dog, Cat, Cow - потомки Animal, у которых в методе speak свои звуки ("Гав", "Мяу", "Мууу")
5. Создайте 4 объекта классов Animal, Dog, Cat, Cow и поместите их в список
6. Пройдитесь циклом по элементам списка и вызовите метод speak для каждого из объектов (элементов списка)

## C. Паттерн фабричный метод
```
from animal import Dog,Cat,Cow
class Fabrica:
    def create(self,type):
        if type == "Dog":
            return Dog("Собака")
        if type == "Cat":
            return Cat("Кошка")
        if type== "Cow":
            return Cow("Корова")
fab = Fabrica()
list_animals= [fab.create("Dog"),fab.create("Cat"), fab.create("Cow")]

for animal in list_animals:
    animal.speak()
```

## D. Работа с git-ом - фиксируем изменения и передаем на удаленный репозиторий
Если программа успешно работает - передайте код на удаленные репозиторий  
   - добавьте файл (в Git Bash) в репозиторий  
     `git add .`  
   - закоммитьте изменения  
     `git commit -m "Added new file"`  
   - создадим новую ветку и переключимся на нее  
     `git checkout -b branch-220124-comp<N>`  
     (где N - номер вашего компа)  
   - `git push --set-upstream origin branch-220124-comp<N>`     
