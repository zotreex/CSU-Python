import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float
from sneakers import Sneakers
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
Base.metadata.create_all(engine)


if __name__ == "__main__":
    new_sneakers = Sneakers(name="test", price=2.55, size=40, brand="Test")
    session.add(new_sneakers)
    # Благодаря этой строчке мы добавляем данные а таблицу
    session.commit()
    for post in session.query(Sneakers):
        print(post)
