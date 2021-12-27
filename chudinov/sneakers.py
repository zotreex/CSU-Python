from sqlalchemy import Column, Integer, String, Float

from chudinov.task3 import Base


class Sneakers(Base):
    __tablename__ = 'Sneakers'
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    price = Column('price', Float)
    size = Column('size', Integer)
    brand = Column('brand', String)

    def __init__(self, name, price, size, brand):
        self.name = name
        self.price = price
        self.size = size,
        self.brand = brand