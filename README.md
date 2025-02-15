# Farpost Parser Project

## Описание

Этот проект на Django предоставляет API для получения данных о первых 10 объявлениях с сайта Farpost по ссылке: [Farpost - Системы видеонаблюдения](https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/).

## Функциональность

- Парсинг данных о первых 10 объявлениях.
- Сохранение данных в базе данных.
- API для получения информации об объявлении по ID.

## Технологии

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
- BeautifulSoup4
- Requests
- Django Rest Framework

## Установка

### Настройка проекта и БД:
создайте файл .env и заполните настройками из env.sample

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/samwance/farpost_parser.git
    cd farpost_parser
    ```

2. Создайте и активируйте виртуальное окружение:

    ```sh
    python -m venv venv
    source venv/bin/activate  # для Windows: venv\Scripts\activate
    ```

3. Установите зависимости:

    ```sh
    pip install -r requirements.txt
    ```

4. Примените миграции:

    ```sh
    python manage.py migrate
    ```

5. Создайте суперпользователя для доступа к админке:

    ```sh
    python manage.py createsuperuser
    ```

6. Запустите сервер разработки:

    ```sh
    python manage.py runserver
    ```

## Использование

В проекте изпользуется авторизация по токену, настроить время токена можно в настройках, получить токн можно по url:
```
POST /token/

Content-Type: application/json

{
    "username": "<USErname>",
    "password": "Password"
}
```

### Парсинг данных

Для парсинга данных с сайта Farpost выполните следующую команду (к сожалению слишком часто нельзя использовать):

```sh
python manage.py parse_ads
```

### Доступ к админке

Перейдите по адресу `http://127.0.0.1:8000/admin/` и войдите в админку с учетными данными суперпользователя.

## Примеры запросов
### Получение списка объявлений
```
GET /
```
Пример вывода списка объявлений в postman
![img.png](media/ads_list.png)
### Получение объявления по ID
```
GET /{id}/
```
Пример вывода объявления по id в postman:
![img.png](media/ad_detail.png)

Так же в корневой папке находится json-файл со всеми данными по объявлениям
