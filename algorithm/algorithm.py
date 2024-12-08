def display_optimal_choice(products):
    if not products:
        return None
    optimal_product = None
    best_ratio = float("inf")

    for product in products:
        if product.rating and product.price:
            ratio = product.price / product.rating
            if ratio < best_ratio:
                best_ratio = ratio
                optimal_product = product

    return optimal_product
