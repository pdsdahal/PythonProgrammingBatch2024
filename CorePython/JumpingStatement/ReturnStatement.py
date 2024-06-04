#Function with returning some values
def add(num1, num2):
    sumResult = num1 + num2
    return sumResult


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


data1 = int(input("Enter a first number "))
data2 = int(input("Enter a second number "))

choice = input("Select the  choice \n 1. + \n 2. *\n 3. / \n 4. - ")
result = 0
if choice == "1":
    result = add(data1, data2)
    print(f"{data1} + {data2} = {result}")
elif choice == "2":
    result = mul(data1, data2)
    print(f"{data1} * {data2} = {result}")
elif choice == "3":
    result = div(data1,data2)
    print(f"{data1} / {data2} = {result}")
else:
    result = sub(data1,data2)
    print(f"{data1} - {data2} = {result}")

