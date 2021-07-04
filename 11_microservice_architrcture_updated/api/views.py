from flask import Flask, request, abort ,jsonify
from models import engine, Post, User, DeclarativeBase
from sqlalchemy.orm import sessionmaker
from settings import logger
import json

DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
app = Flask(__name__)


#curl -d '{"username":"NewUser", "email":"egorich@mail.com", "password": "123"}' -H "Content-Type: application/json" -X POST http://localhost:5000/signup
@app.route("/signup", methods = ["post"])
def signup():
    content = request.get_json()
    
    email = content.get('email') 
    username = content.get('username') 
    password = content.get('password')

    if email and username and password:
        try:
            new_user = User(name=username, email=email, password=password)
            db_session = Session()
            db_session.add(new_user)
            db_session.commit()
            message = f"New user {username} created."
            logger.info(message)
            return jsonify({}), 201
        except Exception as e:
            message = f"User with params {content} not loaded with exception: {e}"
            logger.error(message)
            return jsonify({"error_message": message}), 400


@app.route("/users")
def get_users():
    try:
        db_session = Session()
        users_query = db_session.query(User).all()
        users = [user.serialize for user in users_query]
        res = jsonify(users)
        return res, 200
    except Exception as e:
        message = f"Something went wrong in loading users: {e}"
        logger.error(message)
        res = jsonify({"error_message": message})
        return res, 400


@app.route("/users/<user_id>")
def get_user(user_id): 
    try:
        db_session = Session()
        user = db_session.query(User).filter(User.id == user_id).first()
        if user:
            res = jsonify(user.serialize)
            return res, 200
        else:
            res = {"error_message": f"User with id {user_id} not found"}
            return jsonify(res),404
    except Exception as e:
        message = f"Something went wrong in loading user {user_id} because : {e}"
        logger.error(message)
        return jsonify({"error_message":message}), 400

@app.route("/users/user_by_name/<username>")
def get_user_by_username(username): 
    try:
        db_session = Session()
        user = db_session.query(User).filter(User.name == username).first()
        if user:
            res = jsonify(user.serialize)
            return res, 200
        else:
            res = {"error_message": f"User with id {username} not found"}
            return jsonify(res),404
    except Exception as e:
        message = f"Something went wrong in loading user {username} because : {e}"
        logger.error(message)
        return jsonify({"error_message":message}), 400



@app.route("/posts")
def get_posts():
    try:
        db_session = Session()
        posts_query = db_session.query(Post).all()
        posts = [post.serialize for post in posts_query]
        res = jsonify(posts)
        return res
    except Exception as e:
        message = f"Something went wrong in loading posts: {e}"
        return jsonify({"error_message":message}), 400


@app.route("/posts/<post_id>")
def get_post(post_id): 
    try:
        db_session = Session()
        post = db_session.query(Post).filter(Post.id == post_id).first()
        if post:
            res = jsonify(post.serialize)
            return res, 200
        else:
            res = {"error_message": f"Post with id {post_id} not found"}
            return jsonify(res),404
    except Exception as e:
        message = f"Something went wrong in loading post {post_id}: {e}"
        logger.error(message)
        return jsonify({"error_message": message}), 400


@app.route("/posts/create_post", methods = ["post"])
def create_post():
    content = request.get_json()
    
    title = content.get('title') 
    text = content.get('text') 
    author = content.get('author')
    author = int(author)
    #NOT STRING

    if title and text and author:
        try:
            new_post = Post(text=text, title=title, author=author)
            db_session = Session()
            db_session.add(new_post)
            db_session.commit()
            message = f"New post {new_post.serialize} created."
            logger.info(message)
            res = jsonify(new_post.serialize)
            return res, 201
        except Exception as e:
            message = f"Post {content} not created with exception: {e}"
            logger.error(message)
            return jsonify({"error_message": message}), 400


"""
Tests 
docker-compose
"""