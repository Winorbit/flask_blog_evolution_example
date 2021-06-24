from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from settings import dev_db_settings as db_settings

engine  = create_engine(URL.create(**dev_db_settings))
DeclarativeBase = declarative_base()


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
        return title


DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='NewAuthor', email="author@test.ru", password="mysecret")
new_post = Post(title='Some post title', text="Just some text")

#print(new_user.id)
#new_post = Post(title='Some post title', text="Just some text", author=1)

#session.add(new_user)
#session.add(new_post)
#session.commit()


for user in session.query(User):
    print(user.name)


for post in session.query(Post):
    print(post.title)