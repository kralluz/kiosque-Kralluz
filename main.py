from management.tab_handler import calculate_tab
""" from management.product_handler import (
    get_product_by_id,
    get_products_by_type,
    add_product
    )
"""

if __name__ == "__main__":
    """ print(get_products_by_type('drink'))
    print(get_product_by_id(28))
    print(add_product("lorem inpusm", 12.5, 5, "lorem ipsum", "drink")) """
    print(calculate_tab([{"_id": 1, "amount": 5}, {"_id": 19, "amount": 3}]))
