## Блог подключен к базе данных с использованием ORM.

1) Вместо сырых SQL-запросов используеться ORM SQLAlchemy
2) Данные для подключения к БД вынесены в переменные окружения через .env-файл.
3) Блог распилен на несколько логических кусочков.

### Требования
Python 3.5+
Данные для подключения к Postgres в файле SQLAlchemy/setting.py
Данные для подключения к Postgres в файле blog_with_orm/.env.py

### Запуск

```
cd blog_with_orm
pipenv lock && pipenv sync
pipenv shell
python run.py
```
