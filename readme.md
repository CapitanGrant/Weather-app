# Описание

Это простое веб-приложение на Flask для получения текущей погоды в различных городах.

## Требования

- Python 3.12
- Flask
- Aiohttp
- Pymorphy3

## Установка

1. Скопируйте репозиторий:
    ```bash
    git clone https://github.com/CapitanGrant/Weather-app
    cd weather_app
    ```

2. Создайте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Установите библиотеки:
    ```bash
    pip install -r requirements.txt
    ```

## Установка через Docker

1. Выполните команду, для сборки контейнера
    ```bash
   docker build -t weather-app .
   ```

2. Запустите контейнер
    ```bash
   docker run -p 5000:5000 weather-app
   ```
   
3. Перейдите в браузере по адресу:
    ```bash
   http://localhost:5000
   ```
