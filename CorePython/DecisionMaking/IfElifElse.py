operator = input("Enter a operator to perform operation (+,-,*,/,%)")
num1 = float(input("Enter a first number "))
num2 = float(input("Enter a second number "))
result = 0

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2
else:
    result = num1 % num2

print(f"{num1} {operator} {num2} = {result}")