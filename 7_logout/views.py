from flask import Flask, request, render_template, redirect, session, url_for
from models import engine, Post, User, DeclarativeBase
from sqlalchemy.orm import sessionmaker

DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    db_session = Session()
    posts_query = db_session.query(Post).all()
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
        db_session = Session()
        db_session.add(new_user)
        db_session.commit()

        return redirect(url_for("login"))
    else:
        return render_template('user/signup.html')

@app.route("/login", methods = ["get", "post"])
def login():
    if request.method == 'POST':
        username = request.form.get('username') 
        password = request.form.get('password')
        db_session = Session()
        user = db_session.query(User).filter(User.password == password, 
                                          User.name == username).one()
        if not user:
            message = "Проверьте правильность введенных данных."
            return render_template('user/login.html', message=message)
        else:
            session['username'] = username
            return redirect(url_for('my_cabinet'))
    else:
        message = "Введите данные для того, чтобы войти в личный кабинет."
        return render_template('user/login.html', message=message)


@app.route("/logout", methods = ["post"])
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route("/cabinet", methods = ["get", "post"])
def my_cabinet():
    if request.method == 'POST':
        title = request.form.get('title') 
        text = request.form.get('post_text')

        username = session.get("username")

        db_session = Session()
        user = db_session.query(User).filter(User.name == username).one()

        if user:
            new_post = Post(title=title, text=text, author=user.id)
            db_session.add(new_post)
            db_session.commit()
            return redirect(url_for("my_cabinet"))
        else:
            error_message = "Ваши данные некорректны, для решния проблемы попробуйте авторизоваться заново."
            return render_template('error_page.html',error_message=error_message)

    else:
        if session.get("username"):
            return render_template('user/cabinet.html')
        else:
            return redirect(url_for("login"))

@app.route("/posts")
def posts():
    db_session = Session()
    posts_query = db_session.query(Post).all()
    posts = [post for post in posts_query]
    return render_template('posts/posts.html', posts=posts)
    pass

@app.route("/posts/<post_id>")
def post(post_id):
    db_session = Session()
    post = db_session.query(Post).filter(Post.id == post_id).one()
    return render_template('posts/post.html', post=post)
    pass