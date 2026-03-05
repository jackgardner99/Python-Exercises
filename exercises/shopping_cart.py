shopping_cart_items = []

def average_price(cart_items):
    average_price = 0

    for item in cart_items:
        average_price += item

    try:
        average = average_price / len(cart_items)

        return average
    except ZeroDivisionError as e:
        return 0

average_price_of_cart_items = average_price(shopping_cart_items)

print(f"Your average cart item price is {average_price_of_cart_items} dollars.")