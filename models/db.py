from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
import os

UzumBase = declarative_base()
AmazonBase = declarative_base()
EbayBase = declarative_base()
TechnoBase = declarative_base()


class UzumProducts(UzumBase):
    __tablename__ = "uzum_products"
    id = Column(Integer, primary_key=True)
    marketplace = Column(String, nullable=False, default="uzum")
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=True)


class AmazonProducts(AmazonBase):
    __tablename__ = "amazon_products"
    id = Column(Integer, primary_key=True)
    marketplace = Column(String, nullable=False, default="amazon")
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=True)


class EbayProducts(EbayBase):
    __tablename__ = "ebay_products"
    id = Column(Integer, primary_key=True)
    marketplace = Column(String, nullable=False, default="ebay")
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=True)


class TechnoProducts(TechnoBase):
    __tablename__ = "techno_products"
    id = Column(Integer, primary_key=True)
    marketplace = Column(String, nullable=False, default="techno")
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=True)


def initialize_database():
    uzum_db = "uzum.db"
    amazon_db = "amazon.db"
    ebay_db = "ebay.db"
    techno_db = "techno.db"

    if not os.path.exists(uzum_db):
        uzum_engine = create_engine(f"sqlite:///{uzum_db}")
        UzumBase.metadata.create_all(uzum_engine)
        print(f"{uzum_db} database created successfully")
    else:
        print(f"{uzum_db} already exists.")

    if not os.path.exists(amazon_db):
        amazon_engine = create_engine(f"sqlite:///{amazon_db}")
        AmazonBase.metadata.create_all(amazon_engine)
        print(f"{amazon_db} tables ensured to exist.")
    else:
        print(f"{amazon_db} already exists.")

    if not os.path.exists(ebay_db):
        ebay_engine = create_engine(f"sqlite:///{ebay_db}")
        EbayBase.metadata.create_all(ebay_engine)
        print(f"{ebay_db} database created successfully")
    else:
        print(f"{ebay_db} already exists.")

    if not os.path.exists(techno_db):
        techno_engine = create_engine(f"sqlite:///{techno_db}")
        TechnoBase.metadata.create_all(techno_engine)
        print(f"{techno_db} database created successfully")
    else:
        print(f"{techno_db} already exists.")


initialize_database()
