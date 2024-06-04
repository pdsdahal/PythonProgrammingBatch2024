flag = int(input("enter a range you want to execute the code : "))
sum = 0
for i in range(flag):
    num = int(input("enter a number to find the positive sum  (negative number quit the program) : "))
    if num < 0:
        break
    sum = sum + num
print(f"Sum of positive numbers  = {sum}")