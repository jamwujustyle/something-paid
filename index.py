from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import initialize_database, AmazonProducts, UzumProducts
import random

if __name__ == "__main__":
    amazon_engine = create_engine("sqlite:///amazon.db")
    uzum_engine = create_engine("sqlite:///uzum.db")

    AmazonSession = sessionmaker(bind=amazon_engine)
    UzumSession = sessionmaker(bind=uzum_engine)

    amazon_session = AmazonSession()
    uzum_session = UzumSession()

    products = [
        "iPhone 15",
        "iPhone 14",
        "iPhone 13",
        "iPhone SE",
        "MacBook Pro",
        "MacBook Air",
        "iPad Pro",
        "iPad Air",
        "Samsung Galaxy S23",
        "Samsung Galaxy Z Flip 5",
        "Google Pixel 8",
        "Microsoft Surface Laptop",
        "Dell XPS 13",
        "HP Spectre x360",
        "Asus ZenBook",
        "Lenovo ThinkPad X1",
        "Sony Xperia 5",
        "OnePlus 11",
        "Xiaomi 13",
        "Oppo Find X6 Pro",
        "Nintendo Switch",
        "PlayStation 5",
        "Xbox Series X",
        "Apple Watch Ultra",
        "Samsung Galaxy Watch 6",
    ]

    try:
        for i in range(100):
            name = f"{random.choice(products)} Model {i+1}"
            price = round(random.uniform(100, 3000), 2)
            rating = round(random.uniform(1.0, 5.0), 1)

            amazon_product = AmazonProducts(name=name, price=price, rating=rating)
            uzum_product = UzumProducts(name=name, price=price, rating=rating)

            amazon_session.add(amazon_product)
            uzum_session.add(uzum_product)

            amazon_session.commit()
            uzum_session.commit()
            print("inserted 100 records into both databases.")

    except Exception as ex:
        amazon_session.rollback()
        uzum_session.rollback()
        print(f"error {ex}")
    finally:
        amazon_session.close()
        uzum_session.close()
