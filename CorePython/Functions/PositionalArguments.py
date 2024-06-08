# When you call a function with positional arguments,
# you pass values to the function's parameters in the same order as they
# are defined in the function's definition.

def display_total_price(price, discount):
    discountAmount = price * (discount / 100)
    actualPrice = price - discountAmount
    print(f"Payable Amount : {actualPrice}")
    print(f"Discount Amount : {discountAmount}")


display_total_price(price=2000, discount=13)
