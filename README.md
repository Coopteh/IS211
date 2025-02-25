# Задача
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
