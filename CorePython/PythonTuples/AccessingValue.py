# A Python tuple is a sequence of comma separated items, enclosed in parentheses ().
# The items in a Python tuple need not be of same data type.
# Item from the tuple can be accessed using its index, and cannot be modified, removed or added.

bookInfo = ("R Programming", "Jones John", 1234.56, "Dedicated to xyz uni", "Computer Department")
print(type(bookInfo))
print(bookInfo)

#using loop
for bookIn in bookInfo:
    print(bookIn)


# using while loop

flag = 0
while flag < len(bookInfo):
    print(f"Element at {flag} is {bookInfo[flag]}")
    flag = flag + 1

# using index
print("Index from 0 to last index : ",bookInfo[0:])
print("Index from 1 to 3: ",bookInfo[1:4])
print("Items from index 0 to 1 : ", bookInfo[:2])
print("Last Element : ",bookInfo[-1])