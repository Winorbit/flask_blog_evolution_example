from sqlalchemy import create_engine, Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dev_db_settings = {"dbname":'testdatabase', 
                   "user":'dev_user', 
                   "password":'qwerty', 
                   "host":'31.131.28.206'}

engine = create_engine(f'postgresql+psycopg2://{dev_db_settings["user"]}:{dev_db_settings["password"]}@{dev_db_settings["host"]}/{dev_db_settings["dbname"]}')
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

new_user = User(name='New', email="testmail@test.ru", password="mysecret")
#print(new_user.id)
new_post = Post(title='Some post titl', text="some text", author=1)


#session.add(new_user)
#session.commit()

session.add(new_post)
session.commit()

for user in session.query(User):
    print(user.id)
