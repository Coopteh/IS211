# TODO
1. Открыть в pyCharm папку ~/PycharmPython/IS211/oop1
2. Создать новый файл oop1.py
3. Создать новый класс Animal
class Animal:
     def __init__(self, name, count)
         self.name = name
         self.count = count

     def show_details(self):
         print(f"Животное {self.name} имеет {self.count} ноги")
4. Создать экземпляр класса Animal и вызвать метод show_details()
obj = Animal('корова', 4)
obj.show_details()
5. Если программа успешно работает - передайте код на удаленные репозиторий
   - добавьте файл (в Git Bash) в репозиторий
     git add .
   - закоммитьте изменения
     git commit -m "Added new file"
   - git push --set-upstream origin
   
