# Описание задачи
1. Создать локальный репозиторий на компьютере
используя копию удаленного репозитория IS211
```
git clone https://github.com/Coopteh/IS211
dir
cd IS211
```
2. Создадим новую ветку - для вашего компьютера
   командой `git checkout -b branch-180124-compN`
3. Создайте файл с кодом hello.py
```
> notepad hello.py
print('hello')
```
4. Проверьте `git status` статус файла
5. Добавьте его в лок.репозиторий командой `git add *`
6. Зафиксируйте (закоммитьте) изменения командой `git commit -m "Add hello.py"`
7. Передайте коммит в удаленный репозиторий через `git push --set-upstream origin branch-180124-compN`
