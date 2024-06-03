#Example 1
for i in range(0,10):
    for j in range(0, i+1):
        print(" * ", end="")
    print()

#Example 2:
rows = int(input("Enter the number of rows "))
columns = int(input("Enter the number of columns "))
symbol  = input("Enter the symbol to use ")

for i in range(rows):
    for j in range(i+1):
        print(f" {symbol} ",end="")
    print()
