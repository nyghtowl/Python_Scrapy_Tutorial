from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py 
    Returns sqlalchemy engine instance
    """

    return create_engine(URL(**settings.DATABASE))

def create_deals_table(engine):
    """
    Maps a class that defines structure to postgres
    and takes metadata ou of table to create tables needed
    """

    DeclarativeBase.metadata.create_all(engine)

def Deals(DeclarativeBase):
    """
    Sqlalchemy deals model
    """
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    description = Column('description', String, nullable=True)
    location = Column('location', String, nullable=True)
    category = Column('category', String, nullable=True)
    original_price = Column('original_price', String, nullable=True)
    price = Column('price', String, nullable=True)

    