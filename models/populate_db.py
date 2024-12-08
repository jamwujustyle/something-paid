import random
from .db import AmazonProducts, UzumProducts, EbayProducts, TechnoProducts


def populate_databases(AmazonSession, UzumSession, EbaySession, TechnoSession):
    products_list = [
        "iPhone 15",
        "iPhone 14",
        "iPhone 13",
        "iPhone SE",
        "iPad Pro",
        "iPad Air",
        "MacBook Pro",
        "MacBook Air",
        "Samsung Galaxy S23",
        "Samsung Galaxy Z Flip 5",
        "Google Pixel 8",
        "Google Pixel 7",
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
        "Apple AirPods Pro",
        "Samsung Galaxy Buds 2",
        "Bose QuietComfort 45",
        "Sony WH-1000XM5",
        "Amazon Echo Dot",
        "Google Nest Hub",
        "Amazon Fire TV Stick",
        "Apple TV 4K",
        "Microsoft Xbox Series S",
        "PlayStation 5 Digital Edition",
        "LG OLED C1",
        "Samsung QN90A QLED TV",
        "Sony Bravia XR",
        "Apple iPad Mini",
        "Huawei Mate 50 Pro",
        "Xiaomi Redmi Note 12",
        "Samsung Galaxy Watch 5",
        "Razer Blade 15",
        "HP Omen 16",
        "Alienware x17",
        "Apple Mac Mini M2",
        "Lenovo Legion 5 Pro",
        "MSI GE76 Raider",
        "Oculus Quest 2",
        "Meta Quest Pro",
        "Google Nest Wifi",
        "Ring Video Doorbell Pro 2",
        "Dyson V15 Detect",
        "Roomba i7+",
        "Samsung Galaxy Tab S8",
        "Lenovo Tab P11",
        "Microsoft Surface Pro 9",
        "Acer Predator Helios 300",
        "Dell Alienware Aurora R13",
        "Razer Nari Ultimate",
        "SteelSeries Arctis 7",
        "Sony PlayStation VR",
        "Nintendo Switch OLED",
        "GoPro HERO11 Black",
        "DJI Mini 3 Pro",
        "Sony A7 IV",
        "Canon EOS R5",
        "Fujifilm X-T4",
        "Sony WH-1000XM4",
        "Bose Noise Cancelling Headphones 700",
        "Roku Ultra",
        "TiVo Stream 4K",
        "Apple iPhone 12",
        "Samsung Galaxy S21 Ultra",
        "Google Pixel 6 Pro",
        "Xiaomi Mi 11",
        "Samsung Galaxy Z Fold 4",
        "Oppo Reno 8 Pro",
        "Huawei P50 Pro",
        "Nokia G50",
        "Motorola Edge 20 Pro",
        "OnePlus 9 Pro",
        "Sony Xperia 1 III",
        "ASUS ROG Phone 5",
        "Nvidia GeForce RTX 3080",
        "AMD Ryzen 9 5900X",
        "Intel Core i9-12900K",
        "Apple M2 Chip",
        "Corsair Vengeance LPX RAM",
        "Samsung 970 EVO SSD",
        "Seagate Barracuda HDD",
        "Western Digital My Passport",
        "SanDisk Ultra MicroSD",
        "Logitech MX Master 3",
        "Razer DeathAdder V2",
        "SteelSeries Rival 3",
        "Logitech G502 Hero",
        "Apple Magic Keyboard",
        "Microsoft Surface Keyboard",
        "Bose SoundLink Flex",
        "Sonos One",
        "Harman Kardon Onyx Studio 6",
        "Google Nest Audio",
        "Harman Kardon SoundSticks 4",
        "Sennheiser Momentum 3",
        "Anker Soundcore Liberty 3 Pro",
        "Sony A9F TV",
        "BenQ EW3270U",
        "Epson EcoTank ET-2720 Printer",
        "Canon PIXMA TS5320",
        "Brother HL-L2395DW",
        "Shure SM7B Microphone",
        "Blue Yeti X",
        "Logitech C920 Webcam",
    ]

    amazon_session = AmazonSession()
    uzum_session = UzumSession()
    ebay_session = EbaySession()
    techno_session = TechnoSession()
    try:
        for product_name in products_list:
            amazon_price = round(random.uniform(1500, 2000), 2)
            uzum_price = round(random.uniform(1300, 2000), 2)
            ebay_price = round(random.uniform(1600, 1800), 2)
            techno_price = round(random.uniform(1899, 2300), 2)

            rating_amazon = round(random.uniform(1.0, 5.0), 1)
            rating_uzum = round(random.uniform(1.0, 5.0), 1)
            rating_ebay = round(random.uniform(1.0, 5.0), 1)
            rating_techno = round(random.uniform(1.0, 5.0), 1)

            amazon_product = AmazonProducts(
                name=product_name,
                price=amazon_price,
                rating=rating_amazon,
            )
            uzum_product = UzumProducts(
                name=product_name,
                price=uzum_price,
                rating=rating_uzum,
            )
            ebay_product = EbayProducts(
                name=product_name,
                price=ebay_price,
                rating=rating_ebay,
            )
            techno_product = TechnoProducts(
                name=product_name,
                price=techno_price,
                rating=rating_techno,
            )
            sessions = [amazon_session, uzum_session, ebay_session, techno_session]
            # Add products to their respective sessions
            amazon_session.add(amazon_product)
            uzum_session.add(uzum_product)
            ebay_session.add(ebay_product)
            techno_session.add(techno_product)

        for session in [amazon_session, uzum_session, ebay_session, techno_session]:
            session.commit()

        print("Inserted products into all databases.")

    except Exception as ex:
        [session.rollback() for session in sessions]
        print(f"Error: {ex}")
    finally:
        [session.close() for session in sessions]
