# Atomic Habits Tracker

Это веб-приложение для отслеживания привычек, созданное на основе концепций из книги "Атомные привычки" Джеймса Клира.

## Описание

В 2018 году Джеймс Клир написал книгу "Атомные привычки", в которой он рассматривает методику формирования полезных привычек и избавления от вредных. Это веб-приложение предоставляет инструмент для реализации этих идей, предоставляя пользователям возможность создавать, отслеживать и улучшать свои привычки.

## Основные функции

1. **Регистрация и Авторизация:** Пользователи могут зарегистрироваться, создать учетную запись и войти в систему для управления своими привычками.

2. **Создание Привычек:** Пользователи могут создавать новые привычки, указывая место, время, действие, признаки и другие параметры.

3. **Отслеживание Действий:** Для каждой привычки пользователи могут отмечать выполненные действия, отслеживая их во времени.

4. **Публичные Привычки:** Пользователи могут делиться своими привычками с другими пользователями, делая их публичными для просмотра.

5. **Напоминания и Уведомления:** Система предоставляет уведомления и напоминания для выполнения привычек в указанное время.

## Как получить чат-идентификатор Telegram?

1. Откройте Telegram и найдите бота `@userinfobot`.
2. Запустите бота, нажав на кнопку "Start" или написав ему `/start`.
3. Бот предоставит вам информацию о вашем аккаунте, включая ваш чат-идентификатор (chat_id).
4. Запишите чат-идентификатор.

Ваш чат-идентификатор (chat_id): [ваш_chat_id]


## Технологии

- **Django:** Веб-фреймворк, обеспечивающий серверную часть приложения.
- **Django REST Framework:** Расширение Django для создания API.
- **Celery:** Инструмент для работы с отложенными задачами, используется для отправки уведомлений.
- **Telegram Integration:** Интеграция с мессенджером Telegram для отправки уведомлений.

## Установка и Запуск

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/Igorek95/atomic-habits-tracker.git
    ```

2. Создайте виртуальное окружение и установите зависимости:

    ```bash
    cd atomic-habits-tracker
    python -m venv venv
    source venv/bin/activate  # для Linux / macOS
    .\venv\Scripts\activate  # для Windows
    pip install -r r.txt
    ```

3. Примените миграции:

    ```bash
    python manage.py migrate
    ```

4. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

5. Перейдите по адресу http://localhost:8000/ в вашем веб-браузере.
