from flask import Flask, render_template, request, current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.db import AmazonProducts, UzumProducts, EbayProducts, TechnoProducts
from models.populate_db import populate_databases
from algorithm.algorithm import display_optimal_choice

app = Flask(__name__)

# Set up the database connections
amazon_engine = create_engine("sqlite:///amazon.db")
uzum_engine = create_engine("sqlite:///uzum.db")
ebay_engine = create_engine("sqlite:///ebay.db")
techno_engine = create_engine("sqlite:///techno.db")


AmazonSession = sessionmaker(bind=amazon_engine)
UzumSession = sessionmaker(bind=uzum_engine)
EbaySession = sessionmaker(bind=ebay_engine)
TechnoSession = sessionmaker(bind=techno_engine)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/", methods=["GET"])
def index():
    search_query = request.args.get("search")
    products = []
    optimal_product = None

    if search_query:
        amazon_session = AmazonSession()
        uzum_session = UzumSession()
        ebay_session = EbaySession()
        techno_session = TechnoSession()

        try:
            # Fetch matching products from both databases
            amazon_products = (
                amazon_session.query(AmazonProducts)
                .filter(AmazonProducts.name.like(f"%{search_query}%"))
                .all()
            )
            uzum_products = (
                uzum_session.query(UzumProducts)
                .filter(UzumProducts.name.like(f"%{search_query}%"))
                .all()
            )
            ebay_products = (
                ebay_session.query(EbayProducts)
                .filter(EbayProducts.name.like(f"%{search_query}%"))
                .all()
            )
            techno_products = (
                techno_session.query(TechnoProducts)
                .filter(TechnoProducts.name.like(f"%{search_query}%"))
                .all()
            )

            products = amazon_products + uzum_products + ebay_products + techno_products

            optimal_product = display_optimal_choice(products)

            current_app.logger.debug(f"current data: {optimal_product}")
        finally:
            for session in [amazon_session, uzum_session, ebay_session, techno_session]:
                session.close()
    return render_template(
        "base.html", products=products, optimal_product=optimal_product
    )


if __name__ == "__main__":
    populate_databases(AmazonSession, UzumSession, EbaySession, TechnoSession)
    app.run(debug=True)
