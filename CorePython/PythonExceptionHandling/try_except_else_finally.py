rollNo = [1, 2, 4, 5, 6, 9]

try:
    element = rollNo[0]
    print("Element at index 10 is : ",element)
except IndexError as e:
    print("Error : ",e)

else:
    print("If there is no exception then this block will be executed")

finally:
    print("Finally block always gets executed either exception is generated or not.")
