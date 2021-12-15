# Список задач
![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/IvanGorbunov/TaskList?include_prereleases)
[![Build Status](https://app.travis-ci.com/IvanGorbunov/TaskList.svg?branch=master)](https://app.travis-ci.com/IvanGorbunov/TaskList)

## Запуск

1. Клонировать репозиторий

    ```bash
    git clone https://github.com/IvanGorbunov/TaskList.git
    ```

1. Устранить зависимости:

    ```bash
    pip install -r requirements.txt
    ```

1. Выполнить миграции:

    ```bash
    python3 manage.py makemigrations  
    python3 manage.py migrate
    ```

1. Создать администратора в БД:

    ```bash
    python3 manage.py createsuperuser
    ```

1. Определить переменные среды окружения:

    добавить текстовый файл настроек .env в папку personal_portfolio с содержанием:

    ```python
    DEBUG=False
    SECRET_KEY=<_любая_последовательность_символов_>
    DATABASE_URL=sqlite:///db.sqlite3

    ALLOWED_HOSTS=<_url_сайта_>
    ```

1. Собрать все статические файлы в одно место:

    ```bash
    python3 manage.py collectstatic
    ```

1. Запуск проекта:

    ```bash
    python3 manage.py runserver
    ```
