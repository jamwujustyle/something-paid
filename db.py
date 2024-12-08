from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()


class UzumProducts(Base):
    __tablename__ = "uzum_products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=True)


class AmazonProducts(Base):
    __tablename__ = "amazon_products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=True)


def initialize_database():
    uzum_db = "uzum.db"
    amazon_db = "amazon.db"

    if not os.path.exists(uzum_db):
        uzum_engine = create_engine(f"sqlite:///{uzum_db}")
        Base.metadata.create_all(uzum_engine)
        print(f"{uzum_db} database created successfully")

    if not os.path.exists(amazon_db):
        amazon_engine = create_engine(f"sqlite:///{amazon_db}")
        Base.metadata.create_all(amazon_engine)
        print(f"{amazon_db} database created successfully")
