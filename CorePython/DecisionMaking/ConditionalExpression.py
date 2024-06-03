#one line shortcut for the if else statement (ternary operator)
# syntax:   x if condition is true else Y

age = int(input("Enter your age : "))
result = "You are eligible for vote!" if age >= 16 else "You are not eligible for vote!"
print(result)

#check even and odd
num = int(input("Enter a number : "))
oddEvenResult = "Even" if num%2 == 0 else "Odd"
print(f"{num} is {oddEvenResult}.")