## Блог подключен к базе данных.

1) Подключен к базе данных Postgres.
2) Добавлены сырые SQL-запросы к БД с использованием бибилиотеки psycopg2.
3) html-код страниц вынесен в html-шаблоны.

### Требования
Python 3.5+

Данные для подключения к Postgres в файле db.py

### Запуск

```
pipenv lock && pipenv sync
pipenv shell
python main.py
```
