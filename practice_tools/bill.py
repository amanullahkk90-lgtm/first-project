def calculate_Bill(prices):
    total=sum(prices)
    if total >1000:
        discount=total*0.10
        return discount-total
    else:
        return total