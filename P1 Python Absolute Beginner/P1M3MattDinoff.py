max = float(100)
min = float(1)
price = float(1.99)
    
def prices(max, min, price, order_amount):
    order_amount = float(order_amount)
    if order_amount > max:
        print("Matt Dinoff, enter cheese order weight: ", order_amount)
        print(order_amount, "is more than currently available stock.")
    elif order_amount < min:
        print("Matt Dinoff, enter cheese order weight: ", order_amount)
        print(order_amount, "is below minimum order amount.")
    else:
        print("Matt Dinoff, enter cheese order weight: ", order_amount)
        print(order_amount,"costs $", (order_amount * price))
    return 

order_amount = input("How many orders do you want? ")
prices(max, min, price, order_amount)