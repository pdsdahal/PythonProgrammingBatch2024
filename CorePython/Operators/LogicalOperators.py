num1 = int(input("Enter a first number "))
num2 = int(input("Enter a second number "))

logicalAnd = num1 < 10 and num2 > 2
print(f" {num1} < 10 and {num2} > 2  = {logicalAnd}")

logicalOr = num1 < 10 or num2 > 2
print(f" {num1} < 10 or {num2} > 2  = {logicalOr}")

logicalNot = not(num1 < 10)
print(f" not( {num1} < 10 ) = {logicalNot}")