# using range function
# range(start, stop, step)
# The range() function returns a sequence of numbers,
# starting from 0 by default, and increments by 1 (by default), and ends at a specified number
for x in range(10): # print x = 0 to 9
    print(x)

print("range(3, 10), which means values from 3 to 10 (but not including 10):")
for y in range(3, 10):
    print(y)

print("In reverse way starting from 14 to 2")
for counter in reversed(range(2,15)):
    print(counter)

print("Display odd numbers from 1 to 10")
# specify the increment value by adding a third parameter: range(1, 10, 2):
for flag in range(1, 10, 2):
    print(flag)

print("Using negative increment value")
for chk in range(16, 0, -2):
    print(chk)


# for loop with Strings
print("For loop with Strings")
collegeName = "illinois state university"
for colege in collegeName:
    print(colege)

print("for Loop with Tuples")
numbers = (1, 4, 7, 9, 11, 34, 78, 43)
for num in numbers:
    print(num)

print("For Loop with Lists")
lstData = ["Apple", "Ball", "1234", "Cat"]
for data in lstData:
    print(len(data), data)