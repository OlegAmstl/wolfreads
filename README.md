# CuteBooks
Проект представляет собой приложение для отслеживания статистики прочтения книг. Зарегестрированный пользователь может поставить цель на год сколько книг он планирует прочитать.
Так же они может добавлять в базу книги, которых там нет.

### Используемые технологии:
1. Python 3.10
2. Django 4.1.6
3. HTML 5
4. CSS 3 

### Установка:
1. Склонировать данный репозиторий.
2. Создать виртуальную среду в склонированном репозитории и активировать ее.
```commandline
python3 -m venv venv
```
3. Установить зависимости 
```commandline
pip install -r requirements.txt
source ./venv/bin/activate
```
4. Перейти в директорию cutebooks
```commandline
cd cutbooks
```
5. Провести миграции
```commandline
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
```
6. Создать суперпользователя.
```commandline
python3 manage.py createsuperuser
```
7. Запустить приложение.
```commandline
python3 manage.py runserver
```

#### Автор Маркин Олег