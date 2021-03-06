from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

dev_db_settings = {"drivername": 'postgresql+psycopg2',
                   "database":'database_name', 
                   "username":'database_user', 
                   "password":'database_password', 
                   "host":'database_host'}

engine  = create_engine(URL(**dev_db_settings))
#engine = create_engine(f'postgresql+psycopg2://{dev_db_settings["user"]}:{dev_db_settings["password"]}@{dev_db_settings["host"]}/{dev_db_settings["dbname"]}')

DeclarativeBase = declarative_base()


class User(DeclarativeBase):
    __tablename__ = 'users_2'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    email = Column('email', String)
    password = Column('password', String)

    def __repr__(self):
        return f"{name}"

class Post(DeclarativeBase):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    text = Column('text', String)

    def __repr__(self):
        return title


DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#new_user = User(name='NewAuthor_2', email="authors@test.ru", password="mysxecret")
new_post = Post(title='Some post title', text="Just some text")

#session.add(new_user)
session.add(new_post)
session.commit()

"""
for user in session.query(User):
    print(user.name)


for post in session.query(Post):
    print(post.title)
"""