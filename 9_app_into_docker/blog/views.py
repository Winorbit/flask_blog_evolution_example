from flask import Flask, request, render_template, redirect, session, url_for
from . models import engine, Post, User, DeclarativeBase
from sqlalchemy.orm import sessionmaker
from . settings import logger

DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    db_session = Session()
    try:
        posts_query = db_session.query(Post).all()
        posts = [post for post in posts_query]
        return render_template('main.html', posts=posts)
    except Exception as e:
        error_message = "Something went wrong in loading posts: "
        log_message = f"{error_message}: {e}"
        logger.error(log_message)
        return render_template('error_page.html',error_message=error_message)


@app.route("/signup", methods = ["get", "post"])
def signup():
    if request.method == 'POST':
        email = request.form.get('email') 
        username = request.form.get('username') 
        password = request.form.get('password')

        if email and username and password:
            try:
                new_user = User(name=username, email=email, password=password)
                db_session = Session()
                db_session.add(new_user)
                db_session.commit()
                log_message = f"New user {username} created."
                logger.info(log_message)
                return redirect(url_for("login"))
            except Exception as e:
                error_message = f"User with params {dict(request.form)} not loaded"
                log_message = f"{error_message} with exception: {e}"
                logger.error(log_message)
                return render_template('error_page.html',error_message=error_message)
        else:
            log_message = f"Failed try to create new user {dict(request.form)}."
            logger.error(log_message)
            return redirect(url_for("signup"))
    else:
        return render_template('user/signup.html')


@app.route("/login", methods = ["get", "post"])
def login():
    if request.method == 'POST':
        username = request.form.get('username') 
        password = request.form.get('password')
        if username and password:
            try:
                db_session = Session()
                user = db_session.query(User).filter(User.password == password, 
                                          User.name == username).one()
                if not user:
                    message = "Проверьте правильность введенных данных."
                    return render_template('user/login.html', message=message)
                else:
                    session['username'] = username
                    log_message = f"User {user.name} logged."
                    logger.info(log_message)
                    return redirect(url_for('my_cabinet'))
            except Exception as e:
                log_message = f"Failed logging for user {user.name} with exception: {e}"
                logger.error(log_message)
                return redirect(url_for('login'))
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

        if title and text:
            username = session.get("username")
        else:
            log_message = f"Post with title:{title} and text: {text} not published."
            logger.error(log_message)
        try:
            db_session = Session()
            user = db_session.query(User).filter(User.name == username).one()
            if user:
                new_post = Post(title=title, text=text, author=user.id)
                db_session.add(new_post)
                db_session.commit()
                log_message = f"Post {new_post} published by user {user.id}."
                logger.info(log_message)
                return redirect(url_for("my_cabinet"))
            else:
                error_message = "Ваши данные некорректны, для решния проблемы попробуйте авторизоваться заново."
                return render_template('error_page.html',error_message=error_message)
        except Exception as e:
            log_message = f"Post not published because {e}."
            logger.error(log_message)
            return render_template('user/cabinet.html')
    else:
        if session.get("username"):
            return render_template('user/cabinet.html')
        else:
            return redirect(url_for("login"))


@app.route("/posts")
def posts():
    try:
        db_session = Session()
        posts_query = db_session.query(Post).all()
        posts = [post for post in posts_query]
        return render_template('posts/posts.html', posts=posts)
    except Exception as e:
        error_message = "Something went wrong in loading posts"
        log_message = f"{error_message}: {e}"
        logger.error(log_message)
        return render_template('error_page.html',error_message=error_message)


@app.route("/posts/<post_id>")
def post(post_id): 
    try:
        db_session = Session()
        post = db_session.query(Post).filter(Post.id == post_id).one()
        return render_template('posts/post.html', post=post)
    except Exception as e:
        error_message = f"Something went wrong in loading post {post_id}"
        log_message = f"{error_message}: {e}"
        logger.error(log_message)
        return render_template('error_page.html',error_message=error_message)
