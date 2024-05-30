discount = 0
amount = float(input("Enter your total amount "))
if amount >= 1000:
    discount = (amount * 10) / 100
    amount = amount - discount
    print(f"Your total amount after getting {discount} discount is : {amount}!")

# check postive or negative
num1 = int(input("Enter a integer number : "))
if num1 < 0:
    print(f"Entered number is negative : {num1}")

if num1 > 0:
    print(f"Entered number is positive : {num1}")

if num1 == 0:
    print(f"Entered number is zero : {num1}")