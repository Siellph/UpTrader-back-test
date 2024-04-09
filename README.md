# UpTrader-back-test
django app, реализующий древовидное меню

Установка и запуск проекта

1. Создать виртуальное окружение
```
python -m venv .venv
```
2. Войти в виртуальное окружение
```
. .venv/bin/activate
```
3. Установить зависимости
```
pip install -r requirements
```
4. Выполнить миграции для создания файла БД и таблиц в ней
```
python manage.py migrate
```
5. Создать суперпользователя системы
```
python manage.py createsuperuser
```
6. Загрузить данные из дампа БД
```
python manage.py loaddata dump.json
```
7. Запустить сервер
```
python manage.py runserver
```

Перейти на [локальный сайт](http://127.0.0.1:8000/)

[Панель администрирования](http://127.0.0.1:8000/admin/)
