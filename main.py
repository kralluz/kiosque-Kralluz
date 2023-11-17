from menu import products
from management.tab_handler import calculate_tab
from management.product_handler import (
    get_product_by_id,
    get_products_by_type,
    add_product,
    menu_report
)


if __name__ == "__main__":
    print(get_products_by_type("drink"))
    print(get_product_by_id(28))

    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }

    print(add_product(products, **new_product))
    print(menu_report())
    print(calculate_tab([{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]))
