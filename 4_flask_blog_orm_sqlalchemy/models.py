from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from settings import dev_db_settings as db_settings

DeclarativeBase = declarative_base()
engine  = create_engine(URL.create(**db_settings))


class User(DeclarativeBase):
    __tablename__ = 'users_2'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    email = Column('email', String)
    password = Column('password', String)

    def __repr__(self):
        return "".format(self.email)

class Post(DeclarativeBase):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column('name', String)
    text = Column('email', String)
    author = Column(Integer, ForeignKey('users_2.id'))

    def __repr__(self):
        return self.title

# !! user_posts
# !! запуск через flask
# SQLLAchemy -> FlaskAlchemy
# про то, что это островки знания.
# БД - реляционные - SQL - ORM как обетка
# Дата
# Мои посты
# Изоляция, контейнеризация, ЛОГИ, энвфайлы, трай-эксепт
# API!
# Logogut
# hash username/password
# хэдеры-футеры,часичные шаблоны