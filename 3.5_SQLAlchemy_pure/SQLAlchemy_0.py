from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dev_db_settings = {"dbname":'testdatabase', 
                   "user":'dev_user', 
               	   "password":'qwerty', 
             	   "host":'31.131.28.206'}

engine = create_engine(f'postgresql+psycopg2://{dev_db_settings["user"]}:{dev_db_settings["password"]}@{dev_db_settings["host"]}/{dev_db_settings["dbname"]}')
DeclarativeBase = declarative_base()


class User(DeclarativeBase):
    __tablename__ = 'users'

    #id = Column(Integer, primary_key=True)
    name = Column('name', String)
    email = Column('email', String)

    def __repr__(self):
        return "".format(self.email)

Session = sessionmaker(bind=engine)
session = Session()
for user in session.query(User):
    print(user.id)
