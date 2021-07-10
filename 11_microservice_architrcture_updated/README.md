## Оба микросервиса запакованы в контейнеры.

1) Оба сервиса упакованы в контейнеры, и, для возможности подключаться друг к другу 
   используеться оркестрация контейнеров с помощью docker-compose.

### Требования
Docker
Docker-compose
Данные для подключения к Postgres в [файле]()

### Запуск
Перенос списка зависимостей из Pipenv в requirements.txt :
```
cd api
pipenv lock && pipenv sync
pipenv run pip freeze > requirements.txt

cd web_ui
pipenv lock && pipenv sync
pipenv run pip freeze > requirements.txt
```

Подготовка и запуск в контейнере:
```
sudo docker-compose up --biuld
```