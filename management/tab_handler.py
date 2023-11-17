from management.product_handler import get_product_by_id


def calculate_tab(dictList: list):
    subtotal: dict = {"subtotal": 0.00}

    for item in dictList:
        subtotal["subtotal"] += (
            get_product_by_id(item["_id"])["price"] * item["amount"]
        )

    subtotal["subtotal"] = f'${round(float(subtotal["subtotal"]), 2)}'

    return subtotal
