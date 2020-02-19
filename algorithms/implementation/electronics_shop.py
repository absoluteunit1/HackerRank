def get_money_spent(keyboards, drives, b):
    prices = []
    for k_price in keyboards:
        for d_price in drives:
            if k_price + d_price <= b:
                prices.append(k_price + d_price)
    return max(prices) if len(prices) != 0 else -1
