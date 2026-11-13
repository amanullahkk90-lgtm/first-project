def withdraw_money(balance,amount):
    if amount >balance:
        return"insufficent balance"
    elif amount<=0:
        return "invalid amount"
    else:
        return balance-amount