# Farpost Parser Project

## Описание

Этот проект на Django предоставляет API для получения данных о первых 10 объявлениях с сайта Farpost по ссылке: [Farpost - Системы видеонаблюдения](https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/).

## Функциональность

- Парсинг данных о первых 10 объявлениях.
- Сохранение данных в базе данных.
- API для получения информации об объявлении по ID.

## Технологии

- Python 3.9+
- Django 3.2+
- BeautifulSoup4
- Requests
- Django Rest Framework

## Установка

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

### Парсинг данных

Для парсинга данных с сайта Farpost выполните следующую команду:

```sh
python manage.py parse_ads
```

### Доступ к админке

Перейдите по адресу `http://127.0.0.1:8000/admin/` и войдите в админку с учетными данными суперпользователя.
