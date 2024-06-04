import math

num = int(input("Enter a number to find the next perfect square "))
maxRange = int(input("Enter a maximum range you want to go "))
if num < 0:
    print("Next perfect square is 0.")
elif num == 0:
    print("Next perfect square is 1.")
else:
    for flag in range(num+1,maxRange):
        if math.sqrt(flag).is_integer():
            print(f"Next perfect square is {flag}")
            break
        else:
            continue

