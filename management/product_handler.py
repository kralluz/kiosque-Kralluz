from menu import products


def get_product_by_id(id: int) -> dict:
    for product in products:
        if product["_id"] == id:
            return product


def get_products_by_type(type: str) -> dict:
    products_by_type = []
    for product in products:
        if product["type"] == type:
            products_by_type.append(product)
    return products_by_type


def add_product(
        description: str,
        price: float,
        rating: int,
        title: str,
        type: str
        ):
    id = len(products) + 1
    new_product = dict(
        _id=id,
        description=description,
        price=price,
        rating=rating,
        title=title,
        type=type,
    )
    products.append(new_product)
    print(new_product)
