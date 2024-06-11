# List is one of the built-in data types in Python.
# A Python list is a sequence of comma separated items, enclosed in square brackets [ ].
# The items in a Python list need not be of the same data type.

#Example
studentInfo = ["Ram Pandey", 13, "Saint Louis University", "ram@gmail.com", 1234.45]
print(studentInfo)
print(type(studentInfo))

# Accessing value from List using looping
for info in studentInfo:
    print(info)

# Accessing from index
print("In Index Second : ",studentInfo[2])

# Access List Items with Negative Indexing
# It is used to access elements from the end of a list,
# with -1 referring to the last element, -2 to the second last, and so on.
print("Last Element : ",studentInfo[-1])
print("Second Last Element : ",studentInfo[-2])


# Access List Items with Slice Operator
# start is the starting index (inclusive).
# stop is the ending index (exclusive).
# [start:stop]

print("Items from index 2 to 3 in list1: ", studentInfo[2:4])
print("Items from index 1 to last in list1: ", studentInfo[1:])
print("Items from index 0 to 1 in list2: ", studentInfo[:2])
print("Items from index 0 to index last in list3", studentInfo[:])