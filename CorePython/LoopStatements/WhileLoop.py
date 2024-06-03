i = 0
while i < 10:
    print(i)
    i += 1

#
foodName = input("Enter a food name you like (q to quit)")
while foodName != "q":
    print(f"Your food is : {foodName}")
    foodName = input("Enter another food name you like (q to quit)")
