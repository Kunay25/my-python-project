# My Python Project

Мой первый проект на Python.

## Описание
Практическая работа №4. Настройка среды разработки.

## Запуск программы
python3 app/main.py
## Практическая работа №6. API на FastAPI

В проекте реализовано API для управления книгами и категориями.

Используются:
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy

### Запуск

1. Активировать виртуальное окружение:
   source venv/bin/activate

2. Установить библиотеки:
   pip install -r requirements.txt

3. Настроить файл .env и запустить PostgreSQL.

4. Запустить сервер:
   uvicorn app.main:app --reload

Документация API:
http://127.0.0.1:8000/docs
