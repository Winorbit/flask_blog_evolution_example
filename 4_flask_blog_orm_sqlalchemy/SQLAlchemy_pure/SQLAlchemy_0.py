from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dev_db_settings = {"dbname":'database_name', 
                   "user":'database_user', 
               	   "password":'database_password', 
             	   "host":'database_host'}
#'postgresql+psycopg2://dev_user:qwerty@31.131.28.206/testdatabase'
engine = create_engine(f'postgresql+psycopg2://{dev_db_settings["user"]}:{dev_db_settings["password"]}@{dev_db_settings["host"]}/{dev_db_settings["dbname"]}')
DeclarativeBase = declarative_base()


class User(DeclarativeBase):
    __tablename__ = 'users'

    password = Column('password', String)
    email = Column('email', String)

#    def __repr__(self):
#        return "".format(self.email)

Session = sessionmaker(bind=engine)
session = Session()
session.query(User).all()

