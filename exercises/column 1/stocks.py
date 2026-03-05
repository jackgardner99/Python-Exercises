ticker_symbols = {
    "GM": "General Motors",
    "CAT": "Caterpillar",
    "EK": "Eastman Kodak"
}

purchases = [
    ('GM', 100, '10-sep-2001', 48),
    ('CAT', 100, '1-apr-1999', 24),
    ('GM', 200, '1-jul-1998', 56),
    ('EK', 150, '24-aug-2003', 45),
    ('CAT', 200, '31-dec-2000', 13),
    ('GM', 100, '28-oct-2002', 30),
    ('GM', 100, '20-sept-2000', 34),
    ('CAT', 50, '21-may-2002', 45),
    ('EK', 80, '13-apr-2000', 45),
    ('EK', 200, '15-mar-2001', 56),
    ('CAT', 150, '14-feb-2002', 23)
]

def display_purchases():
    print("List of all purchases")
    print("---------------------")
    for purchase in purchases:
        product = purchase[1] * purchase[3]
        name = ticker_symbols.get(purchase[0])
        print(f"{name} stock purchased for ${product}")

display_purchases()

stock_purchases_group = {}

def add_to_stock_purchases_group():
    for ticker in ticker_symbols:
        for purchase in purchases:
            if purchase[0] in ticker:
                stock_purchases_group.setdefault(ticker, []).append(purchase)


add_to_stock_purchases_group()
print(stock_purchases_group)

def total_holdings():
    for group, values in stock_purchases_group.items():
        total = 0
        for purchase in values:
            product = purchase[1] * purchase[3]
            total = product + total
        print(f"{group} Holdings: ${total}")


total_holdings()