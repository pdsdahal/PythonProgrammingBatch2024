rollNo = [1, 2, 4, 5, 6, 9]

try:
    element = rollNo[10]
    print("Element at index 10 is : ",element)

finally:
    print("Finally block always gets executed either exception is generated or not.")
