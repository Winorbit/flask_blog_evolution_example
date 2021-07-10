from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dev_db_settings = {"dbname":'database_name', 
                   "user":'database_user', 
                   "password":'database_password', 
                   "host":'database_host'}

engine = create_engine(f'postgresql+psycopg2://{dev_db_settings["user"]}:{dev_db_settings["password"]}@{dev_db_settings["host"]}/{dev_db_settings["dbname"]}')
DeclarativeBase = declarative_base()


class User(DeclarativeBase):
    __tablename__ = 'users_2'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    email = Column('email', String)

    def __repr__(self):
        return "".format(self.email)

DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


#new_user = User(name='New', email="testmail@test.ru")
#session.add(new_user)
#session.commit()


for user in session.query(User):
    print(user.name)



