Обернут в Докер
Логика вынесена отдельно
абсолютный_путь

pipenv lock && pipenv sync
pipenv run pip freeze > requirements.txt
sudo docker build -t blog_image:bot_image . && sudo docker run -d -p blog_image:bot_image
