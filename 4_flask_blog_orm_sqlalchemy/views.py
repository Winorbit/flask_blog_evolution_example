"""
https://gadjimuradov.ru/post/sqlalchemy-dlya-novichkov/
https://habr.com/ru/post/470285/
"""
from flask import Flask, request, make_response, render_template, redirect
from models import engine, Post, User, DeclarativeBase
from sqlalchemy.orm import sessionmaker

DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    session = Session()
    posts_query = session.query(Post).all()
    posts = [post for post in posts_query]
    return render_template('main.html', posts=posts)
    pass

@app.route("/signup", methods = ["get", "post"])
def signup():
    if request.method == 'POST':
        email = request.form.get('email') 
        username = request.form.get('username') 
        password = request.form.get('password')

        new_user = User(name=username, email=email, password=password)
        session = Session()
        session.add(new_user)
        session.commit()

        res = make_response(redirect("/login"))
        return res
    else:
        return render_template('signup.html')

@app.route("/login", methods = ["get", "post"])
def login():
    if request.method == 'POST':
        username = request.form.get('username') 
        password = request.form.get('password')
        session = Session()
        user = session.query(User).filter(User.password == password, 
                                          User.name == username).one()
        if not user:
            message = "Проверьте правильность введенных данных."
            return render_template('login.html', message=message)
        else:
            res = make_response(redirect("/cabinet", code=302))
            res.set_cookie('username', username)
            return res
    else:
        message = "Введите данные для того, чтобы войти в личный кабинет."
        return render_template('login.html', message=message)

@app.route("/cabinet", methods = ["get", "post"])
def my_cabinet():
    if request.method == 'POST':
        title = request.form.get('title') 
        text = request.form.get('post_text')

        username = request.cookies.get("username")

        session = Session()
        user = session.query(User).filter(User.name == username).one()

        if user:
            new_post = Post(title=title, text=text, author=user.id)
            session.add(new_post)
            session.commit()
            res = make_response(redirect("/cabinet"))
            return res
        else:
            error_message = "Ваши данные некорректны, для решния проблемы попробуйте авторизоваться заново."
            return render_template('error_page.html',error_message=error_message)

    else:
        if request.cookies.get("username"):
            return render_template('cabinet.html')
        else:
            error_message = "В ваших cookie-файлах не найдено данных о пользователе, пожалуйста, залогиньтесь еще раз."
            return render_template('error_page.html',error_message=error_message)
            pass
            
    


