# SunriseTestWork

Создайте виртуальное окружение и активируйте:

- python3 -m venv venv
- . venv/bin/activate

Установите все зависимости по команде:

- pip install -r requirements.txt

В данном приложении используется база данных PostgrSQL, так что создайте базу данных:

- create database "database name" owner "database user";

Делаем соответствующие миграции для моделей:

- python3 manage.py makemigrations
- python3 manage.py migrate

Создаем админа для админ панели:

- python3 manage.py createsuperuser

Запускаем проект локально, и заходим в админ панель и создаем тестовые продукты и категории:

- python3 manage.py runserver

Замечание, есть скрытый .env файл, так что замените все скрытые значения (SECRET_KEY и т.д.) на свои.

