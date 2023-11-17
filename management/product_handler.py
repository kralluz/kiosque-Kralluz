from menu import products
from typing import List
from collections import Counter


def get_product_by_id(id: int) -> dict:
    if not isinstance(id, int):
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == id:
            return product

    return {}


def get_products_by_type(type: str) -> dict:
    if not isinstance(type, str):
        raise TypeError("product type must be a str")
    products_by_type = []

    for product in products:
        if product["type"] == type:
            products_by_type.append(product)

    return products_by_type


def add_product(list_products: List[dict], **new_product) -> dict:
    if not list_products:
        new_product["_id"] = 1
    else:
        product_max_id = max(list_products, key=lambda x: x["_id"])
        new_product["_id"] = product_max_id["_id"] + 1
    list_products.append(new_product)

    return new_product


def menu_report():
    sum_prices = 0
    type_count = Counter(product["type"] for product in products)
    most_common_type = type_count.most_common(1)[0][0]

    for product in products:
        sum_prices += product["price"]

    if sum_prices > 0:
        media = sum_prices / len(products)
        media = round(float(media), 2)
    else:
        media = "not enough values to calculate the average"

    teste = f"Products Count: {len(products)} - Average Price: ${media} - Most Common Type: {most_common_type}"
    return teste
