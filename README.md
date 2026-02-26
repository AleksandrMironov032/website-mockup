# NASA web-site

Тестовое задание на Django 5.2 + MySQL + Bootstrap 5.

## Запуск проекта

1. Клонировать репозиторий
2. Создать виртуальное окружение и активировать его
3. Установить зависимости:
   pip install -r req.pip
4. Создать базу данных MySQL:
   CREATE DATABASE myproject CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
5. Настроить подключение к БД в config/settings.py
6. Применить миграции:
   python manage.py migrate
7. Создать суперпользователя:
   python manage.py createsuperuser
8. Запустить сервер:
   python manage.py runserver

## Админка
Доступна по адресу /admin/
Слайды добавляются и сортируются через drag&drop