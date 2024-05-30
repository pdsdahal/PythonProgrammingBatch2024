num1 = int(input("Enter a number "))

if num1 > 0:
    if (num1 % 2) == 0:
        if(num1 % 3) == 0:
            print(f"{num1} is divisible by 2 and 3!")
        else:
            print(f"{num1} is divisible by 2 and not by 3!")
    elif (num1 % 4) == 0:
        print(f"{num1} is divisible by 4!")
    else:
        print(f"{num1} is not divisible by 2 and 4!")
