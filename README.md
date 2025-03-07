# Задача 1
Установка сервера PostgreSQL и графической оболочки pgAdmin  
Загрузите виртуальную машину с Ubuntu и выполните команды
```
sudo apt update
sudo apt install postgresql -y
sudo apt install postgresql-contrib -y

Проверьте что сервис запущен
service postgresql status

Зайдите под юзером postgres
sudo -i -u postgres
psql
Выполните команды
\l
\du
ALTER USER postgres WITH PASSWORD 'qwerty';
\q
```
Установите графическую оболочку pgAdmin
```
sudo apt install curl -y
# Install the public key for the repository (if not done previously):
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

# Create the repository configuration file:
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

# Install for both desktop and web modes:
sudo apt install pgadmin4 -y
```
Запустите pgAdmin и создайте новый сервер
```
name: localhost
addres: 127.0.0.1
user: postgres
pass: qwerty
```
Видео по теме [Установка PostgreSQL и pgAdmin4 на Linux Ubuntu](https://www.youtube.com/watch?v=kWUW3sMK0Mk)   
Видео по теме [Создание таблиц в PostgreSQL с помощью pgAdmin 4](https://www.youtube.com/watch?v=h5wgbJiSy7Q)

# Задача 2 
Работа с графической оболочкой pgAdmin 4   
```
В pgAdmin4 создайте базу данных: demo

Для нее создайте 2 таблицы (Schema \ public\ Tables):
goods, поля:
 product_id integer
 name text
 category integer
 price numeric
categories, поля:
 category_id integer
 name text

Резервирование - для базы данных demo вызовите контекстное меню и создайте резервную копию \Backup
Удалите обе таблицы
Восстановление - для базы данных demo вызовите контекстное меню и восстановитесь из резервной копии \Restore
```

Создание резервной копии и восстановление из терминала  
```

```
